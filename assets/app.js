(function(){
var EMAIL="minitinfotech@gmail.com";
var t=document.querySelector(".mb"),m=document.getElementById("menu");
if(t)t.addEventListener("click",function(){var o=m.classList.toggle("open");t.setAttribute("aria-expanded",o)});
var y=document.getElementById("yr");if(y)y.textContent=new Date().getFullYear();
var f=document.getElementById("qf");if(!f)return;
var pre=new URLSearchParams(location.search).get("cat");if(pre&&f.cat)f.cat.value=pre;
f.addEventListener("submit",function(e){
e.preventDefault();if(f.website.value)return;
var bad=0,first;
f.querySelectorAll("[data-req],[name=phone]").forEach(function(el){
var v=el.value.trim(),er=el.parentNode.querySelector(".err"),msg="";
if(el.type==="checkbox"){if(!el.checked)msg="Please acknowledge the privacy notice."}
else if(!v){if(el.name!=="phone")msg="This field is required."}
else if(el.type==="email"&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v))msg="Enter a valid email address.";
else if(el.name==="phone"&&v.replace(/\D/g,"").length<8)msg="Enter a valid phone number.";
el.setAttribute("aria-invalid",!!msg);er.textContent=msg;
if(msg){bad++;first=first||el}});
if(bad){first.focus();return}
var d=new FormData(f),b=[];
["name","company","email","phone","country","cat","brand","qty","timing","msg"].forEach(function(k){b.push(k.toUpperCase()+": "+(d.get(k)||"-"))});
var ok=document.getElementById("ok");ok.style.display="block";
ok.textContent="Thank you. Your email app will open with your enquiry ready to send. If it does not, email us at "+EMAIL+" or message us on WhatsApp.";
location.href="mailto:"+EMAIL+"?subject="+encodeURIComponent("Quote request: "+(d.get("cat")||"General"))+"&body="+encodeURIComponent(b.join("\n"));
f.reset()});
})();
