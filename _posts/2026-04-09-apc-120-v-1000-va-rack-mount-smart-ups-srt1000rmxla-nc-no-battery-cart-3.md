---
title: APC 120 V 1000 VA Rack-Mount Smart-UPS SRT1000RMXLA-NC NO BATTERY (Cart 3)
date: 2026-04-09
tags:
  - ups
  - rack-mount
  - apc
  - smart-ups
  - 120v
  - no-battery
  - data-center
  - home-lab
---

![APC SRT1000RMXLA image](/assets/images/srt1000rmxla.jpg)

Introduction

If you run a home lab that occasionally pretends to be a data center or manage a small office network where a single reboot can cause a cascade of chaos, you have met the APC SRT1000RMXLA-NC. This is the 120 V 1000 VA rack-mount Smart-UPS in a no battery configuration. Cart 3 means you might be tempted to treat this as a bargain, but remember the old wisdom about UPS gear: what you save on the shelf, you pay in the dark when the lights flicker and your server farm politely asks for a heroic rescue mission from a power outage. In Geeknite style, we will break down what this unit is, what it pretends to be, and what it actually needs to be worth the investment.

What is the SRT1000RMXLA-NC?

The SRT1000RMXLA-NC is part of APC’s Smart-UPS RT family, a line that aims to combine rugged data center features with the convenience of a rack-mount chassis. The SRT prefix signals Smart-UPS Runtime capabilities, while RMXLA indicates a rack-mount model intended for the North American market. The NC suffix stands for no battery, which is not a convenience feature so much as a shipping quirk or an optional configuration in certain sales channels. In the field, you will encounter two realities: the chassis itself, which is a sturdy metal loaf of uptime potential, and a battery pack that you must source separately if you ever intend to run your devices on battery.

Relatable example: you can buy this unit to act as a power conditioning station and a surge protector with clean, regulated output, but you cannot count on it for real runtime until a BR-series battery pack or equivalent is installed. That means Cart 3 is a reminder that UPS shopping sometimes comes with a second to-do list: obtain the compatible battery kit and verify compatibility with your load profile before you pretend to be a hero on outage night.

Build quality and design

APC has a reputation for industrial-grade build quality, and the SRT1000RMXLA-NC is no exception in terms of chassis robustness. Expect a metal frame, a rack ears kit, and a compact 2U footprint that can nestle into a standard 19-inch rack. The front panel is dominated by an LCD or LED display depending on the exact revision, plus status indicators for power, battery, overload, and communication. The unit’s weight is non-trivial, designed to stay put in a rack even when the apartment’s power wants to pretend it’s auditioning for a physics class on inertia.

The no-battery caveat aside, the enclosure feel communicates that this is a device built to live in 24/7 environments. It’s not a cosmetic piece you leave on top of a closet; it’s a field tool that your servers rely on during the occasional heroic reboot.

Key specifications (typical values and what they mean in practice)

- Capacity: 1000 VA / ~700 W (for planning, assume 700 W as the rough practical limit for typical servers and networking gear). This is enough to gracefully power a small rack or a handful of virtual machines in a home lab during short outages.
- Output: Clean, regulated 120 V AC with AVR to compensate for under- and over-voltage events. AVR (automatic voltage regulation) helps ride the line without dropping into battery mode for minor fluctuations.
- Input: 120 V nominal, 60 Hz, auto-sensing. This makes the unit compatible with North American power standards and reduces the risk of misfiring on a poorly wired outlet.
- Form factor: 2U rack-mount chassis with front-loading access to the battery bay (when a battery pack is connected) and rear-access cables for power, USB, and optional network management.
- Battery configuration: No battery installed by default in this NC variant. You will need to purchase a compatible BR-series battery pack or an OEM replacement to unlock runtime and keep the UPS functional if you want to use it beyond static line conditioning.
- Management interfaces: USB for local monitoring; serial or network options may be available via a Network Management Card (not always included). Expect typical APC software support like PowerChute for shutdown orchestration, plus integration with SNMP tools if you add the right management card.
- Output waveform: True sine wave in most configurations, suitable for a broad range of sensitive equipment.
- Protections: Surge suppression, short-circuit protection, overload protection, and a steady clockwork of self-tests. It is designed to ride the chaos and keep your gear from joining a random restart party.
- Cooling and acoustics: Within a 2U design, fans engage to maintain thermal stability. You may notice a background hum during heavy load, but it should be manageable in most data centers and dedicated home labs.

What does no battery really mean in practice?

If you buy the SRT1000RMXLA-NC without a battery, you are buying the chassis, internals, firmware, and the ability to regulate voltage and surge protect. You are not buying runtime. In practical terms, that means:

- The UPS will regulate voltage and provide protection from surges long as it is plugged into a powered outlet. It will not be able to supply power during an outage unless a battery pack is installed.
- You cannot reliably test uptime without the battery in place. If you intend to run a server or router during a blackout, ensure you have the battery pack on hand and installed before you flip the switch to On.
- Battery availability and replacement cost are real-world considerations. BR-series batteries vary by model and capacity, but you should budget for a battery kit that can supply runtime for your load profile.
- Battery replacement intervals depend on usage and environment; expect to replace a BR-series battery about every 3 to 5 years in non-ideal environments. In a closet with low humidity and controlled temperature, you might extend that to the longer end of the spectrum, but don’t bank on it.

Installation and initial setup

Setting up the SRT1000RMXLA-NC is straightforward if you have done a rack install before. Here is a practical checklist you can follow:

1) Rack installation. Mount the unit using the included rack ears kit. Ensure the rack is level and properly grounded. Locking wheels can be handy if you need to move the rack, but for a UPS, fixed positioning is usually safer.
2) Power connections. Connect the UPS to a dedicated AC outlet. Do not overload the circuit; the last thing you want is your UPS tripping its own breaker while you are trying to save a server from a power hiccup.
3) Management configuration. If you have a Network Management Card or USB connection, install the management software. Configure shutdown scripts, alerting thresholds, and test your notification channels.
4) Battery installation. If you have a battery pack, install it per the manufacturer’s instructions. Ensure the pack is compatible with the SRT1000RMXLA-NC. Some models require a firmware update to recognize a new battery pack; follow APC’s instructions to complete the integration.
5) Load test. With a reputable load tested, power up your connected devices and perform a controlled test of the outage scenario. Do not attempt this in a production environment without proper change management and backups.

Battery kit options and compatibility

The no-battery variant pushes you toward a battery kit purchase. The BR-series battery packs are common choices that APC typically recommends for their Smart-UPS RT line. When you buy a battery pack, verify:

- Compatibility with the SRT1000RMXLA-NC model (check the exact part number). 
- The battery pack’s vendor warranty and the unit’s firmware compatibility. In some cases, a firmware update can improve battery recognition and runtime accuracy.
- The expected runtime under your typical load. A 700 W load will drain the battery faster than a lighter load, so plan accordingly.

Monitoring and management features

Even without a battery installed, the SRT1000RMXLA-NC offers several essential management features that can improve uptime. The USB port allows local monitoring and controlled shutdowns in case you lose network connectivity. If you add a Network Management Card, you gain remote monitoring, email or SNMP alerts, and the ability to power cycle devices remotely. APC’s software ecosystem can help you track battery health, count cycles, and identify when a replacement battery is due. If you are running a small office or a home lab, the monitoring layer is often more valuable than the runtime option alone.

For readers who want to dive deeper into UPS monitoring philosophy, see our related posts on UPS maintenance and choosing the right unit for your environment. Read more in our UPS maintenance guide and in the post about choosing a UPS for a home lab [UPS Maintenance Guide]({% post_url 2025-05-10-ups-maintenance.html %}) and [Choosing the Right UPS for a Home Lab]({% post_url 2024-12-01-home-lab-ups.html %}).

Real-world performance and testing impressions

In a typical home lab scenario, you want a unit that keeps your network gear safe during voltage sags and minor surges while offering a reasonable chance of surviving a longer outage after a battery pack is connected. The SRT1000RMXLA-NC excels at the first part: robust protection, clean output, and reliable surge tolerance. The second part depends entirely on whether you have installed a compatible battery pack. In other words, this chassis does the part of the job that does not require a battery, but it cannot do the job that requires stored energy without the battery installed.

In practical tests, you can expect:
- Fast response to voltage dips, with AVR lifting lags quickly to keep connected devices safe.
- Clean output waveform suitable for sensitive devices like NAS, virtualization hosts, switches, routers, and the occasional workstation.
- Predictable thermal behavior once the fans engage at moderate loading levels. It should remain quiet enough for a small office, especially if placed in a well-ventilated rack cavity.
- When used with a battery pack, you’ll observe a usable runtime that scales roughly with load. A 700 W load might offer under an hour of runtime in ideal conditions; more realistic numbers depend on battery health and exact pack size.

Internal fans and cooling dynamics

The SRT1000RMXLA-NC uses a pair of cooling fans designed to manage thermal loads. In a rack with a moderate ambient temperature, fans stay relatively quiet and ramp gradually as the unit approaches its thermal limit. If you run a dense rack with multiple high-wattage devices in a hot room, expect louder operation as the fans spin up to maintain safe temperatures. This is normal for 2U rack-mount UPS devices and not a sign of poor design. It is simply the price of keeping a pile of servers alive without melting a motherboard in the process.

Pro tips for maximizing uptime and lifespan

- Place the UPS in a cool, dry environment with good airflow. A hot closet is not a friendly place for electronics, even if they are designed to handle surges.
- Plan your battery replacement schedule. Batteries have limited lifespans. A well-maintained schedule reduces the chance of an outage becoming a disaster because the battery failed mid-flight.
- Use the UPS in a role-appropriate way. If you do not need runtime, you can use the unit for voltage regulation and protection. If you do need runtime, ensure a battery pack is installed and tested regularly.
- Regularly update firmware when APC releases updates that address reliability or compatibility with new devices and operating systems. Firmware updates can fix bugs that affect monitoring, reporting, and battery management.

Interlinking with other posts and resources

- For more on keeping your environment sane during outages, check our UPS maintenance guide. It covers battery health checks, self-test scheduling, and alert thresholds that help you stay ahead of problems before they become drama.
- We also have a practical guide on selecting the right UPS for a home lab, including storage considerations for batteries, runtime estimates, and how to budget for maintenance.
- If you want to compare models side by side, our post on alternatives to the APC Smart-UPS family discusses what to look for in a unit and how to map features to your workload.

What customers should know before buying

- The no-battery variant is designed for buyers who either want to reuse an existing battery pack or who want to pay a lower upfront cost and source the battery kit separately. If you need immediate uptime under outage conditions, you will want to purchase the battery kit alongside the chassis.
- Availability and pricing for BR-series or equivalent battery packs can vary by region and retailer. If you are shopping online, verify compatibility with the exact SRT1000RMXLA-NC model and confirm warranty coverage for both the chassis and the battery pack.
- In a business setting, ensure your procurement includes proper installation services if you are not comfortable with rack mounting and battery installation. A failed battery or improper wiring can lead to avoidable downtime.

External references and product pages

- APC official product page: https://www.apc.com/us/en/products/smart-ups-srt-1000va/
- Battery compatibility guide: https://www.apc.com/us/en/support/article/FA152719
- A general overview of the SRT series and its place in the APC lineup: https://en.wikipedia.org/wiki/Smart-UPS

Conclusion and final assessment

The APC 120 V 1000 VA Rack-Mount Smart-UPS SRT1000RMXLA-NC NO BATTERY is a solid chassis that offers reliable protection, robust build quality, and scalable management for a home lab or small data center environment. The no-battery variant is not a complete package by itself; it is a component of a broader solution. If you plan to deploy it as a runtime-capable UPS, you must pair it with an appropriate BR-series battery pack and perform firmware compatibility checks. If your need is mostly protection, surge suppression, and voltage regulation, with no requirement for backup power, the NC version can be a cost-efficient choice as long as you understand the limitations and plan accordingly.

Final verdict

- Pros: sturdy build, reliable protection, soft start and AVR for voltage regulation, compact 2U rack-mount form factor, clear monitoring options with USB.
- Cons: no battery included by default, runtime depends entirely on battery availability, requires extra purchase for full uptime capabilities, firmware and compatibility checks recommended for best integration.
- Overall: a strong choice for a modest rack environment where you are prepared to add a battery pack. If you want runtime out of the box, look for a battery-equipped SKU or factor in the cost of the BR-series battery kit.

Where to buy and final note

If you are ready to add this to your rack, the APC SRT1000RMXLA-NC is a dependable option that balances protection with future-proofing for a growing lab. For readers who appreciate a bit of Geeknite humor with their hardware decisions, remember: you only become an IT superhero once your gear survives the outage and your coffee remains untouched. For those who want to support the site and grab this unit through our preferred partners, use the affiliate link below and join the ranks of people who have mastered the art of being prepared without actually powering up the device without a battery installed.

**Shop the APC Smart-UPS SRT1000RMXLA-NC via our affiliate link: https://example-affiliate.com/geeknite/apc-srt1000rmxla-nc?ref=geeknite**
