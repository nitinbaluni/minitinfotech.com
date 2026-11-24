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

  // Pre-select the product category when arriving from a product page, e.g. contact.html?category=iphones
  var categoryMap = {
    "mobile-phones": "Mobile Phones",
    "iphones": "iPhones",
    "accessories": "Accessories",
    "smart-devices": "Smart Devices"
  };
  var requested = new URLSearchParams(window.location.search).get("category");
  var categorySelect = form.elements.category;
  if (categorySelect && requested && categoryMap[requested]) {
    categorySelect.value = categoryMap[requested];
  }

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
    var field = function (key) {
      return String(formData.get(key) || "").trim();
    };

    // The lead service receives name, company, email, phone and message.
    // The extra business details are added to the message so nothing is lost.
    var details = [
      "Business type: " + field("businessType"),
      "Product category: " + field("category"),
      "Brand / model: " + (field("brandModel") || "-"),
      "Required quantity: " + (field("quantity") || "-"),
      "Delivery city / PIN code: " + field("delivery")
    ].join("\n");
    var requirement = field("msg");

    var payload = {
      formType: "contact",
      name: field("name"),
      company: field("company"),
      email: field("email"),
      phone: field("phone"),
      message: details + (requirement ? "\n\nRequirement details:\n" + requirement : ""),
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
        "Thank you for contacting Minit Infotech. Your business enquiry has been received. Our team will review your requirements and get in touch.",
        false
      );
      form.reset();
    } catch (error) {
      showStatus(
        "We couldn't submit your enquiry. Please try again or contact us directly by phone, WhatsApp or email.",
        true
      );
    } finally {
      if (submitButton) {
        submitButton.disabled = false;
        submitButton.removeAttribute("aria-busy");
        submitButton.textContent = submitButton.dataset.originalText || "Submit Business Enquiry";
      }
    }
  });
}());
