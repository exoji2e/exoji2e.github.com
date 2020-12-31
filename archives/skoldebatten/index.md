---
layout: page
title: "Arkiv - Skoldebatten"
---

<style>
ul {
    margin: 10px;
    padding: 5px;
}
p {
    margin-bottom: 5px;
}
</style>

Jag har länge följt debatten om marknadsskolan, och kritiken mot skolpengssystemet. Framför allt via [Tankesmedjan Balans](https://tankesmedjanbalans.se/). 

Den 17:e november to verkligen debatten fart i och med Filippa Mannerheims debattartikel i Expressen: [Svensk skola är en skam – ni politiker har svikit](https://www.expressen.se/kultur/svensk-skola-ar-en-skam-ni-politiker-har-svikit/)

Nedan har jag samlat de {{ site.data.archive.skoldebatten | size }} opinionstexter under 2020 (och framåt) jag kunnat hitta som är kritiska till nuvarande ekonomiska styrsystem av skolan i Sverige. Har jag missat din debattartikel? Den kan enkelt tas med genom att [maila](mailto:exoji2e@gmail.com) eller [twittra](https://twitter.com/exoji2e) till mig.

{% for article in site.data.archive.skoldebatten %}
- {{ article.date }} : 
[{{ article.title }}]({{ article.url }}) 
({{ article.source }})
{% endfor %}