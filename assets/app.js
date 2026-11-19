(function () {
  "use strict";
  
  var SUPPORT_EMAIL = "minitinfotech@gmail.com";
  var API_ENDPOINT = "https://minitinfotech-api.013-nitin.workers.dev/api/leads";

  var toggle = document.querySelector(".mb");
  var menu = document.getElementById("menu");

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var isOpen = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(isOpen));
    });
  }

  var year = document.getElementById("yr");
  if (year) year.textContent = new Date().getFullYear();

  var form = document.getElementById("qf");
  if (!form) return;

  var submitButton = form.querySelector('[type="submit"]');
  var status = document.getElementById("ok");

  function showStatus(message, isError) {
    if (!status) return;
    status.textContent = message;
    status.style.display = "block";
    status.setAttribute("role", isError ? "alert" : "status");
    status.setAttribute("aria-live", "polite");
    status.classList.toggle("error", Boolean(isError));
  }

  function clearErrors() {
    form.querySelectorAll(".err").forEach(function (node) {
      node.textContent = "";
    });
    form.querySelectorAll('[aria-invalid="true"]').forEach(function (node) {
      node.removeAttribute("aria-invalid");
    });
  }

  function setFieldError(field, message) {
    field.setAttribute("aria-invalid", message ? "true" : "false");
    var wrapper = field.closest(".f") || field.parentElement;
    var error = wrapper ? wrapper.querySelector(".err") : null;
    if (error) error.textContent = message;
  }

  function validate() {
    clearErrors();
    var firstInvalid = null;
    var invalid = false;

    form.querySelectorAll("[data-req]").forEach(function (field) {
      var message = "";
      if (field.type === "checkbox") {
        if (!field.checked) message = "Please acknowledge the privacy notice.";
      } else {
        var value = field.value.trim();
        if (!value) message = "This field is required.";
        else if (field.type === "email" &&
                 !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(value)) {
          message = "Enter a valid email address.";
        }
      }

      if (message) {
        setFieldError(field, message);
        invalid = true;
        if (!firstInvalid) firstInvalid = field;
      }
    });

    var phone = form.elements.phone;
    if (phone && phone.value.trim()) {
      var digits = phone.value.replace(/\D/g, "");
      if (digits.length < 8 || digits.length > 15) {
        setFieldError(phone, "Enter a valid phone number.");
        invalid = true;
        if (!firstInvalid) firstInvalid = phone;
      }
    }

    if (firstInvalid) firstInvalid.focus();
    return !invalid;
  }

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    if (status) {
      status.style.display = "none";
      status.textContent = "";
    }

    // Honeypot field: silently stop likely bot submissions.
    var honeypot = form.elements.website;
    if (honeypot && honeypot.value.trim()) return;

    if (!validate()) return;

    var formData = new FormData(form);
    var payload = {
      formType: "contact",
      name: String(formData.get("name") || "").trim(),
      company: String(formData.get("company") || "").trim(),
      email: String(formData.get("email") || "").trim(),
      phone: String(formData.get("phone") || "").trim(),
      message: String(formData.get("msg") || "").trim(),
      consent: formData.get("consent") === "on",
      sourcePage: window.location.pathname
    };

    if (submitButton) {
      submitButton.disabled = true;
      submitButton.setAttribute("aria-busy", "true");
      submitButton.dataset.originalText = submitButton.textContent;
      submitButton.textContent = "Sending...";
    }

    try {
      var response = await fetch(API_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      var result;
      try {
        result = await response.json();
      } catch (_) {
        result = {};
      }

      if (!response.ok || !result.success) {
        throw new Error(
          result.message || "We couldn't submit your enquiry. Please try again."
        );
      }

      showStatus(
        "Thank you. Your enquiry has been submitted successfully. Our team will contact you soon.",
        false
      );
      form.reset();
    } catch (error) {
      showStatus(
        (error && error.message ? error.message : "Unable to submit your enquiry.") +
          " You can also email " + SUPPORT_EMAIL + ".",
        true
      );
    } finally {
      if (submitButton) {
        submitButton.disabled = false;
        submitButton.removeAttribute("aria-busy");
        submitButton.textContent = submitButton.dataset.originalText || "Send Enquiry";
      }
    }
  });
}());
