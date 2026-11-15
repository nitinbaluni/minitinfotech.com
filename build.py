# Generates the static pages. Edit CONTACT values, then run: python3 build.py
PHONE="+91 00000 00000"; TEL="+910000000000"; WA="910000000000"; EMAIL="info@minitinfotech.com"
NAV=[("index.html","Home"),("about.html","About Us"),("products.html","Products"),("brand-partners.html","Brand Partners"),("b2b-supply.html","B2B Supply"),("contact.html","Contact Us")]
I={"phone":'<path d="M7 2h10a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1zM11 18h2"/>',
"plug":'<path d="M9 2v6M15 2v6M6 8h12v3a6 6 0 0 1-12 0zM12 17v5"/>',
"watch":'<rect x="6" y="6" width="12" height="12" rx="3"/><path d="M9 6l1-4h4l1 4M9 18l1 4h4l1-4M12 10v2l1.5 1"/>',
"chat":'<path d="M21 12a8 8 0 0 1-11.5 7.2L3 21l1.8-6A8 8 0 1 1 21 12z"/>',
"doc":'<path d="M6 2h9l5 5v15H6zM14 2v6h6M9 13h8M9 17h8"/>',
"box":'<path d="M21 8l-9-5-9 5v8l9 5 9-5zM3 8l9 5 9-5M12 13v8"/>',
"team":'<circle cx="9" cy="8" r="3.5"/><path d="M2 21c0-4 3-6 7-6s7 2 7 6M17 4.5a3.5 3.5 0 0 1 0 7M22 21c0-3-1.5-5-4-5.8"/>'}
def ic(n):return f'<div class="ic" aria-hidden="true"><svg viewBox="0 0 24 24">{I[n]}</svg></div>'
def page(fn,title,desc,body,hero=False):
    nav="".join(f'<li><a href="{h}"{" aria-current=page" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta name="theme-color" content="#10243A">
<link rel="preload" href="assets/inter.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="assets/manrope.woff2" as="font" type="font/woff2" crossorigin><link rel="icon" href="assets/favicon.png"><link rel="stylesheet" href="assets/style.css"></head><body>
<a href="#main" class="hp" onfocus="this.className='btn p'" style="position:absolute">Skip to content</a>
<header><div class="w nav"><a href="index.html" aria-label="Minit Infotech home"><img src="assets/logo.webp" width="440" height="{{LH}}" alt="Minit Infotech"></a>
<nav aria-label="Main"><button class="mb" aria-label="Menu" aria-expanded="false" aria-controls="menu"><span></span></button><ul id="menu">{nav}<li><a class="btn p" href="request-a-quote.html">Request a Quote</a></li></ul></nav></div></header>
<main id="main">{body}</main>
<footer><div class="w"><div class="grid"><div><div class="tile"><img src="assets/logo.webp" width="440" height="{{LH}}" alt="Minit Infotech" loading="lazy"></div><p>Technology supply, built for business. Mobile phones, accessories and smart devices for B2B buyers.</p></div>
<div><h3>Explore</h3><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in NAV)}</ul></div>
<div><h3>Contact</h3><ul><li><a href="tel:{TEL}">{PHONE}</a></li><li><a href="https://wa.me/{WA}">WhatsApp</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
<div><h3>Legal</h3><ul><li><a href="request-a-quote.html">Request a Quote</a></li><li><a href="privacy-policy.html">Privacy Policy</a></li><li><a href="terms.html">Terms &amp; Conditions</a></li></ul></div></div>
<p class="copy">© <span id="yr">2026</span> Minit Infotech. All rights reserved. All brand names belong to their respective owners.</p></div></footer>
<a class="wa" href="https://wa.me/{WA}" aria-label="Chat on WhatsApp"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:8px">{I["chat"]}</svg><span>WhatsApp</span></a>
<script src="assets/app.js" defer></script></body></html>'''
def head(e,h,p):return f'<section class="sec dark"><div class="w"><p class="eyebrow">{e}</p><h1>{h}</h1><p class="lead" style="color:#c9d6df;margin-top:14px">{p}</p></div></section>'
def band(h,p,b,l):return f'<section class="sec dark band"><div class="w"><h2>{h}</h2><p>{p}</p><div class="cta"><a class="btn p" href="{l}">{b}</a></div></div></section>'
CATS=[("phone","Mobile Phones","Smartphones and feature phones for retail and resale, sourced to your requirement.","mobile-phones"),
("plug","Accessories","Chargers, cables, cases, audio and everyday add-ons for retail counters and bulk buyers.","accessories"),
("watch","Smart Devices","Smart watches, wearables and connected gadgets for growing technology retailers.","smart-devices")]
def cards():return "".join(f'<article class="card">{ic(i)}<h3>{n}</h3><p>{d}</p><a class="more" href="{q}.html">Explore {n} →</a></article>' for i,n,d,q in CATS)
phone_svg='''<svg viewBox="0 0 400 440" role="img" aria-label="Illustration of a smartphone, earbuds and smart watch"><circle cx="200" cy="220" r="170" fill="#ffffff12"/><rect x="120" y="50" width="160" height="320" rx="26" fill="#0b1a2a" stroke="#12A89D" stroke-width="4"/><rect x="132" y="70" width="136" height="280" rx="14" fill="#1a3a58"/><rect x="170" y="58" width="60" height="7" rx="3.5" fill="#12A89D"/><rect x="148" y="100" width="104" height="14" rx="7" fill="#ffffff30"/><rect x="148" y="128" width="64" height="10" rx="5" fill="#ffffff20"/><rect x="148" y="170" width="46" height="46" rx="12" fill="#12A89D"/><rect x="206" y="170" width="46" height="46" rx="12" fill="#ffffff30"/><rect x="148" y="228" width="46" height="46" rx="12" fill="#ffffff30"/><rect x="206" y="228" width="46" height="46" rx="12" fill="#ffffff20"/><rect x="40" y="250" width="74" height="74" rx="20" fill="#0b1a2a" stroke="#fff" stroke-width="3"/><circle cx="77" cy="287" r="20" fill="#1a3a58" stroke="#12A89D" stroke-width="3"/><path d="M77 275v13l8 5" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M300 300a28 28 0 0 1 56 0v34a14 14 0 0 1-28 0" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/><circle cx="300" cy="300" r="10" fill="#12A89D"/></svg>'''

QF="request-a-quote.html"
def form():return """<form id="qf" novalidate><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="f"><label for="n">Name <b>*</b></label><input id="n" name="name" autocomplete="name" data-req><span class="err" role="alert"></span></div>
<div class="f"><label for="c">Company</label><input id="c" name="company" autocomplete="organization"></div>
<div class="f"><label for="e">Business email <b>*</b></label><input id="e" name="email" type="email" autocomplete="email" data-req><span class="err" role="alert"></span></div>
<div class="f"><label for="p">Phone / WhatsApp</label><input id="p" name="phone" type="tel" autocomplete="tel"><span class="err" role="alert"></span></div>
<div class="f"><label for="ct">Product category <b>*</b></label><select id="ct" name="cat" data-req><option value="">Select…</option><option>Mobile Phones</option><option>Accessories</option><option>Smart Devices</option><option>Other</option></select><span class="err" role="alert"></span></div>
<div class="f"><label for="co">Country / destination</label><input id="co" name="country"></div>
<div class="f"><label for="b">Brand / model</label><input id="b" name="brand"></div>
<div class="f"><label for="q">Quantity</label><input id="q" name="qty"></div>
<div class="f full"><label for="t">Target timing</label><input id="t" name="timing" placeholder="e.g. within 2 weeks"></div>
<div class="f full"><label for="m">Message / requirements</label><textarea id="m" name="msg" rows="4"></textarea></div>
<div class="f full"><label style="display:flex;gap:10px;font-weight:500;align-items:flex-start"><input type="checkbox" name="consent" data-req style="width:20px;min-height:20px;margin-top:3px"><span>I agree to Minit Infotech using these details to respond to my enquiry. See the <a href="privacy-policy.html">Privacy Policy</a>.</span></label><span class="err" role="alert"></span></div>
<div class="full"><button class="btn p" type="submit">Send Enquiry</button></div><div class="ok full" id="ok" role="status"></div></form>"""
BR=[("Brand name","Mobile Phones"),("Brand name","Mobile Phones"),("Brand name","Accessories"),("Brand name","Accessories"),("Brand name","Smart Devices"),("Brand name","Smart Devices"),("Brand name","Accessories"),("Brand name","Mobile Phones")]
def brands(n):return '<div class="brands">'+"".join(f'<div class="brand"><b>{a}</b><small>{c}</small></div>' for a,c in BR[:n])+'</div>'
P={}
P["index.html"]=("Minit Infotech | Technology Supply. Built for Business.","Minit Infotech supports B2B enquiries for mobile phones, accessories and smart devices through a straightforward quote process.",
f"""<section class="hero dark"><div class="w g"><div><p class="eyebrow">B2B technology supply</p><h1>Technology Supply. Built for Business.</h1>
<p class="lead">Minit Infotech supports business enquiries for mobile phones, accessories and smart devices through a straightforward B2B process.</p>
<div class="cta"><a class="btn p" href="request-a-quote.html">Request a Quote</a><a class="btn s l" href="products.html">Explore Products</a></div></div>{phone_svg}</div></section>
<div class="strip"><div class="w"><ul><li>Mobile phones, accessories, smart devices</li><li>Retailers, resellers and corporate buyers</li><li>Quotes on request</li><li>Phone, WhatsApp and email</li></ul></div></div>
<section class="sec"><div class="w"><div class="head"><p class="eyebrow">Product categories</p><h2>What we supply</h2><p class="lead">Tell us the category, quantity and destination. We respond with relevant availability and quotation details.</p></div><div class="grid">{cards()}</div></div></section>
<section class="sec soft"><div class="w"><div class="head"><p class="eyebrow">Brand partners</p><h2>Brands &amp; Product Ecosystem</h2><p class="lead">Explore selected technology brands and product categories relevant to our B2B supply enquiries. Contact us to discuss current availability and requirements.</p></div>{brands(4)}<p style="margin-top:28px"><a class="btn s" href="brand-partners.html">View Brand Partners</a></p></div></section>
<section class="sec"><div class="w"><div class="head"><p class="eyebrow">Why Minit Infotech</p><h2>Practical, transparent, business-first</h2></div><div class="grid">
<div class="card">{ic("chat")}<h3>Responsive enquiries</h3><p>Reach us by phone, WhatsApp or email.</p></div>
<div class="card">{ic("doc")}<h3>Clear quotations</h3><p>Straightforward quotes and documentation.</p></div>
<div class="card">{ic("box")}<h3>Product-focused</h3><p>Concentrated on phones, accessories and smart devices.</p></div>
<div class="card">{ic("team")}<h3>Business communication</h3><p>Written for buyers, resellers and procurement teams.</p></div></div></div></section>
<section class="sec soft"><div class="w"><div class="head"><p class="eyebrow">How it works</p><h2>From requirement to dispatch</h2></div><ol class="steps" style="padding:0">
<li><h3>Requirement</h3><p>Share category, model, quantity and destination.</p></li><li><h3>Quote</h3><p>Receive availability and pricing.</p></li><li><h3>Confirmation</h3><p>Agree terms and documentation.</p></li><li><h3>Dispatch</h3><p>Goods ship with the paperwork.</p></li></ol></div></section>
{band("A Clear Process for Business Enquiries","Tell us what you need, including product category, quantity and destination. We'll review your enquiry and respond with relevant availability and quotation details.","Discuss Your Requirement",QF)}""")
P["about.html"]=("About Us | Minit Infotech","Minit Infotech is an India-based B2B technology supplier focused on clear communication with business buyers.",
head("About us","Technology Supply, Built Around Business Needs","We work with business buyers who want a clear, responsive way to enquire about technology products.")+
f"""<section class="sec"><div class="w two"><div class="prose"><h2>Who we are</h2><p>Minit Infotech is an India-based business supporting enquiries for mobile phones, accessories and smart devices from retailers, resellers, wholesalers and corporate buyers.</p><p>We focus on understanding your requirement, sharing relevant availability and quotations, and communicating clearly through the order.</p></div>
<div class="grid" style="grid-template-columns:1fr"><div class="card"><h3>Our mission</h3><p>Make technology sourcing simple and transparent for business customers.</p></div><div class="card"><h3>How we operate</h3><ul class="tick"><li>Clear, honest communication</li><li>Written quotations and documentation</li><li>Prompt follow-up on every enquiry</li></ul></div></div></div></section>
{band("Let's talk about your requirement","Our team is happy to answer questions about categories and ordering.","Contact Our Team","contact.html")}""")
P["products.html"]=("Products | Mobile Phones, Accessories, Smart Devices | Minit Infotech","Product categories supported by Minit Infotech. Ask about current availability.",
head("Products","Product Categories","Brand and model availability may vary. Ask us for current stock and terms.")+
f'<section class="sec"><div class="w"><div class="grid">{cards()}</div></div></section>'+band("Need something specific?","Send us the brand, model, quantity and destination.","Ask About Availability",QF))
TYPES={"mobile-phones":("Mobile Phones","Smartphones and feature phones for retail, resale and corporate requirements.",["Smartphones","Feature phones","Tablets (on request)","Bulk and corporate orders"]),
"accessories":("Accessories","Everyday add-ons for retail counters and bulk buyers.",["Chargers and cables","Cases and screen protection","Audio and earphones","Power banks"]),
"smart-devices":("Smart Devices","Connected devices for growing technology retailers and business buyers.",["Smart watches","Fitness bands","Smart home basics","Other connected gadgets"])}
for k,(n,d,l) in TYPES.items():
    P[k+".html"]=(f"{n} | Minit Infotech",f"{n} supply enquiries for business buyers: {d}",
    head(n,n,d)+f'<section class="sec"><div class="w two"><div class="prose"><h2>Product types</h2><ul class="tick">'+"".join(f"<li>{x}</li>" for x in l)+f'</ul><p class="note">Product types are indicative. Confirm current brands, models and availability by enquiry.</p></div><div class="card">{ic("box")}<h3>Check availability</h3><p>Share the brand, model and quantity you need.</p><a class="btn p" href="request-a-quote.html?cat={n.replace(" ","+")}">Check Availability</a></div></div></section>')
P["brand-partners.html"]=("Brands & Product Ecosystem | Minit Infotech","Selected technology brands and product categories relevant to Minit Infotech B2B supply enquiries.",
head("Brand partners","Brands &amp; Product Ecosystem","We work with business buyers on enquiries across selected technology brands and product categories.")+
f"""<section class="sec"><div class="w">{brands(8)}<p class="note">Brand and model availability may vary. Contact us for current stock and commercial terms. Brand names shown do not imply official partnership or authorisation.</p></div></section>
{band("Looking for a specific brand or model?","Share the brand, model, quantity and destination. We'll review your requirement and discuss the next steps.","Request a Quote",QF)}""")
P["b2b-supply.html"]=("B2B Supply | Minit Infotech","How retailers, resellers, wholesalers and corporate buyers can enquire with Minit Infotech.",
head("B2B supply","A Clear Process for Business Enquiries","A simple enquiry-to-quotation process for trade customers.")+
f"""<section class="sec"><div class="w two"><div class="prose"><h2>Who we serve</h2><ul class="tick"><li>Retailers and resellers</li><li>Wholesalers and distributors</li><li>Corporate and institutional buyers</li></ul><h2>What to include in your enquiry</h2><ul class="tick"><li>Category or brand/model</li><li>Quantity</li><li>Destination</li><li>Timing and documentation needs</li></ul></div>
<ol class="steps" style="padding:0;grid-template-columns:1fr"><li><h3>Enquiry</h3><p>Send your requirement.</p></li><li><h3>Quotation</h3><p>We share availability and pricing.</p></li><li><h3>Order &amp; terms</h3><p>Confirm details and documentation.</p></li><li><h3>Dispatch</h3><p>Your order is shipped.</p></li></ol></div></section>
{band("Ready to work together?","Tell us what you need and we will respond with next steps.","Become a Trade Partner",QF)}""")
P["request-a-quote.html"]=("Request a Quote | Minit Infotech","Send a B2B quote request for mobile phones, accessories or smart devices to Minit Infotech.",
head("Request a quote","Request a Quote","Share your requirement and we'll respond with the next steps.")+f'<section class="sec"><div class="w prose" style="max-width:820px">{form()}</div></section>')
P["contact.html"]=("Contact Us | Minit Infotech","Contact Minit Infotech by phone, WhatsApp or email.",
head("Contact","Contact Us","Reach our team directly or send an enquiry.")+
f"""<section class="sec"><div class="w two"><div><h2 style="margin-bottom:20px">Send an enquiry</h2>{form()}</div>
<div><h2 style="margin-bottom:20px">Get in touch</h2><ul class="ci"><li><small>Phone</small><a href="tel:{TEL}">{PHONE}</a></li><li><small>WhatsApp</small><a href="https://wa.me/{WA}">Chat with us</a></li><li><small>Email</small><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div></div></section>""")
P["privacy-policy.html"]=("Privacy Policy | Minit Infotech","How Minit Infotech handles information submitted through its website.",
f"""<section class="page"><div class="w prose"><h1>Privacy Policy</h1><p class="note">Draft for review. Have it checked against your actual practices before launch.</p>
<h2>Information we collect</h2><p>When you submit an enquiry we receive the details you provide: name, company, email, phone, country, product interest, quantity, timing and message.</p>
<h2>How we use it</h2><p>We use this information only to respond to your enquiry and manage the resulting business relationship.</p>
<h2>Sharing and retention</h2><p>We do not sell your information. We keep enquiry records only as long as needed for business purposes.</p>
<h2>Contact</h2><p>For questions or deletion requests, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>""")
P["terms.html"]=("Terms & Conditions | Minit Infotech","Website terms for Minit Infotech.",
f"""<section class="page"><div class="w prose"><h1>Terms &amp; Conditions</h1><p class="note">Draft for review. Have it checked by a legal professional before launch.</p>
<h2>Website use</h2><p>Information on this site is for general guidance. Availability, specifications and prices change and are confirmed only in a written quotation.</p>
<h2>Quotations and orders</h2><p>Orders are subject to written confirmation and agreed terms. Enquiries do not create a binding contract.</p>
<h2>Trademarks</h2><p>Brand names mentioned belong to their owners. Their use does not imply endorsement or authorisation.</p>
<h2>Contact</h2><p>Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>""")
from PIL import Image
w,h=Image.open("assets/logo.webp").size
for fn,(t,d,b) in P.items():
    open(fn,"w").write(page(fn,t,d,b).replace("{LH}",str(h)))
open("robots.txt","w").write("User-agent: *\nAllow: /\n")
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>https://YOUR-DOMAIN/{f}</loc></url>" for f in P)+"</urlset>")
