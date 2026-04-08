---
layout: post
title: APC 120 V 1000 VA Rack-Mount Smart-UPS SRT1000RMXLA-NC NO BATTERY (Cart 3)
date: 2026-04-08
tags:
  - ups
  - APC
  - rack-mount
  - smart-ups
  - srt-series
  - uninterruptible-power-supply
  - review
---

![APC SRT1000RMXLA-NC]( /assets/images/apc-srt1000rmxla-nc.jpg )

Introduction: Gear Up Your Lab Without a Battery? Welcome to the Brave New World of APC's Smart-UPS SRT line in No-Battery configuration. If you’re the kind of person who enjoys a good mechanical keyboard click, a dramatic unboxing, and then immediately asks, But where is the battery?, you’re in for a treat. The SRT1000RMXLA-NC is the rack-mountable, 120 V, 1000 VA workhorse that begs for a battery pack like a dragon begs for gold—except here, the gold is the battery that actually makes the thing usable as a UPS. In Cart 3 terms: you’re getting the shell first; the magical juice is sold separately. And no, this post will not pretend that you can simply will a battery into existence through sheer enthusiasm. We are geeks, not wizards.

External links and references (for the curious):
- APC official product family: https://www.apc.com/us/en/products/smart-ups-srt-series/
- General UPS buying guide: https://www.geeknite.example/ups-buying-guide
- A post about installation discipline in the lab: <a href="{% post_url 2024-05-12-ups-installation-guide %}">UPS Installation Guide</a>
- Another Geeknite post on lab power planning: <a href="{% post_url 2025-02-01-lab-ups-strategy %}">Lab Power Strategy for Nerds</a>

H2: What you actually get and what you don’t
The acronym SRT stands for Smart-UPS Ringing The Bell at the Data Center — or something like that. The SRT1000RMXLA-NC is the 1000 VA rack-mount version, designed to live in a 2U rack and talk to your servers, NAS, and RGB-lit coffee maker with equal disdain and affection. The big catch is the NC suffix: no battery. That’s not a melodramatic marketing term; it’s a real thing. APC ships this unit without the backup energy storage module, meaning you’ll have to get the battery pack separately and install it in order to actually ride through a power outage. If you’re on a budget and want to test the UPS vibe before committing to a complete battery plan, this is a sane way to go about it—just don’t pretend the UPS can save your 4K exports without a battery attached.

Pros and cons in plain nerd-speak:
- Pros:
  - Pure sine wave output, which means it plays nicely with modern servers and sensitive electronics.
  - Rack-friendly form factor that makes you feel like a data center rock star when you mount it in your lab rack.
  - Management features that let you monitor, shut down safely, and automate the heroics when the power blinks.
- Cons:
  - Battery not included. You will have to budget for a battery pack. Also, you’ll probably need a battery vendor who speaks fluent charge and cycle counts.
  - If you’re in a power grid with frequent outages, you’d better plan for a battery replacement every 3–5 years depending on use.
  - Initial cost can feel like a two-stage rocket: buy the shell, then the brain and the heart. But that split is how APC keeps modular upgrades alive.

The no-battery approach has its pros and cons, and geeks love a modular upgrade path. The lack of a battery means you’re buying future-proofing, not just a plug-and-play hero. If you’re a modular tinkerer who wants to pick and choose a battery chemistry, brand, and cycle life, the NC edition is the clean slate you deserve.

H2: Build quality and design: a hardware hug from APC
APC’s SRT line is known for sturdy construction, and the 2U chassis of the SRT1000RMXLA-NC reflects that. The metal rails are hefty, the card-edge connectors are robust, and the overall assembly gives you the same confidence you get when you tighten a screw and don’t hear it rattle. The “no battery” concept is a bit unromantic at first glance, but it makes sense when you view the device as a platform rather than a final product. Think of it as a frame for your own energy storage sculpture.

Inside the unit, the power electronics look clean and accessible. The outlets are arranged with practical spacing, allowing bulky European plugs to coexist with US brick adaptors without a fuss if you’re in a multi-country lab. Response controls, LED indicators, and the control panel live in the front for quick status checks during a late-night server cleanup or a ritual reboot.

H2: Battery reality check: what you need to know before you buy
If you’re shopping the NC variant, you’re probably thinking: How much battery do I need to keep the data gods appeased during a blackout while my lab demands keep humming? The short version: you need to buy a battery pack separately. APC offers battery packs and RBC kits designed for their UPS family. The exact model you choose affects runtime, cycle life, and maintenance windows. A reasonable approach is to estimate runtime at typical load (say 300–500 W for a small server rack plus a monitoring PC) and then compare the cost of a replacement battery every few years against a complete new UPS investment.

Upside of starting with a bare frame:
- You can tailor the battery capacity to exactly your risk tolerance and budget.
- You can swap in newer battery chemistries as they become financially viable.
- You can keep the rest of your power management ecosystem intact while you decide on the heart and lungs.

Downside:
- It’s a two-step purchase, which means more planning and more procurement tickets in your queue.
- You’ll want to avoid the classic lab scenario where you assume the UPS will magically boot with a battery you forgot to buy.

H2: Installation and first power-on: a ritual for the brave
The physical install is straightforward. Mount the SRT1000RMXLA-NC into a 2U rack, wire it to mains power per your local electrical code, and connect your load to the UPS outputs. The front panel offers a quick glance at output voltage, load level, and battery status once you’ve installed the battery pack. If you’re running a Windows or Linux lab, you’ll want to install the PowerChute or PowerChute Network Shutdown family to get graceful shutdowns and event logging.

Initial configuration steps typically include:
- Setting the input voltage reference (if your grid is not a clean 120 V) and enabling AVR to smooth minor voltage fluctuations.
- Configuring notification emails or snmp traps if you’re using a centralized monitoring system.
- Calibrating the system to your load so that the runtime estimates reflect your actual usage rather than marketing guesses.

H3: Power management and software: PowerChute and friends
Power management is where UPSs earn their keep in a modern lab. The SRT series works with APC’s suite of software, which includes PowerChute for Windows and Linux, and in some cases can integrate with SNMP-based dashboards or third-party monitoring stacks. With the 120 V input and pure sine wave output, you can expect clean handoffs to your servers and virtualization hosts during power events. A nice touch is the ability to configure UPS shutdown times, graceful process termination, and post-event reports that help you prove to stakeholders that you aren’t just pressing the snooze button on the power event.

Pro tip: enable the automatic safe shutdown for all critical VMs and containers, and use the event history to identify any nuisance outages that occur during maintenance windows. You’ll be amazed how often a power blip happens when someone is rebooting a switch at 3 AM in a non-synchronized manner.

H2: Real-world performance: how the SRT1000RMXLA-NC behaves in a lab
In a typical lab scenario, a 1000 VA UPS with 120 V input is enough to cover several modest devices during a short outage. But this NC variant invites you to think about runtime planning as a two-part problem: first, the battery selection; second, the actual load on the UPS. If you’re running a small NAS, a couple of servers, and a monitoring station, you can reasonably expect 5–15 minutes of outage protection with an adequately sized battery. If your lab uses a few desktop machines as well, you’ll want to target the lower end of that range and adjust your expectations accordingly.

One interesting observation is the efficiency curve with AVR engaged. In many environments, you’ll find that the UPS maintains clean sine wave output with light loads, thanks to the AVR, and you’ll see the efficiency creep up as the system stabilizes. That matters because you don’t want to waste energy just because you’re in a place with a power grid that behaves like a moody dragon.

H2: Compatibility, networks, and integration in mixed environments
The APC SRT1000RMXLA-NC is designed to play nicely with a range of equipment and management ecosystems. It supports standard USB and serial connections for local management, and, depending on the optional network card, you can monitor and control the unit over IP. This makes it a sensible choice for lab admins who manage both Windows servers and Linux boxes, plus network gear. When you’re building a rack ecosystem, you want devices that can be discovered by your monitoring stack without requiring a PhD in UPS configuration.

If you’re integrating with a larger lab, you might also be interested in a few internal posts on the same site:
- <a href="{% post_url 2024-08-20-ups-setup-guide %}">UPS Setup Guide for Small Labs</a>
- <a href="{% post_url 2025-11-02-virtualization-power-planning %}">Virtualization Power Planning</a>

H2: Comparing with the competition: what’s the SRT bring to your lab bench?
When you compare the SRT1000RMXLA-NC to other 1 kVA rack UPS offerings, a few points stand out:
- Pure sine wave output at the price point is a big win for sensitive equipment.
- The rack-mount form factor makes it easier to fit into compact lab racks or home lab setups where space is a premium.
- The modular approach (shell without battery) invites a more thoughtful investment: you’re not paying for energy storage you don’t need yet, which can be a cost saver if you’re starting a lab or upgrading in stages.

In terms of raw performance, you’ll typically see similar protection features across reputable brands. The differentiating factor for many geeks is the software integration, the ease of remote monitoring, and the quality of the user interface on the front panel. APC has historically put thought into these areas, and the NC variant is no exception.

H2: The caveats: what to watch out for when you buy the NC model
- Battery selection and availability: Not all battery packs are created equal. Make sure you choose a compatible pack that matches your runtime expectations and cycle life goals.
- Replacement cycle: Over time, batteries wear out. Plan for periodic checks and a budget for replacements to avoid a scenario where you rely on a failing unit during a blackout.
- Documentation: Because this is a modular system, keep good records of which battery model you’ve installed, when you installed it, and the expected replacement window. It makes future procurement a lot easier.
- Rack power considerations: Ensure your rack’s electrical infrastructure can handle any in-rack power issues. If you’re in a space with a shared power strip or limited wiring, you may want to run a dedicated line or ensure the UPS is the primary device on the circuit.

H2: Practical dosing: runtime, load, and return on investment
Let’s talk numbers with a pinch of reality. Suppose you’ve got:
- Load: around 400–600 W (servers, NAS, a monitor, a lab PC)
- Battery pack installed: yes, sized for approximately 5–15 minutes of runtime at this load

Under these conditions, the SRT1000RMXLA-NC can provide a quick hand-off from outage to safe shutdown, ensuring that long-running exports finish gracefully and that research data doesn’t disappear into the aether. If your lab workload includes longer blackouts or heavier loads, you’ll need to adjust your battery capacity accordingly. The key is to pair the UPS with a well-thought-out shutdown policy and a realistic assessment of your grid reliability.

H2: Internal ecosystem notes: how this fits into a Geeknite-style lab setup
For Geeknite readers, power is not an afterthought; it’s a feature. This UPS fits into a lab where you’re running:
- A handful of servers or virtualization hosts
- A NAS or storage appliance
- A few desktop machines for development and testing
- A couple of network devices (switches, routers, firewall)

The no-battery variant doesn’t obstruct this workflow; instead, it invites you to design your own energy strategy and to be selective about what you plug into the UPS. This is a good reminder that in tech, as in life, you don’t want to be a hero with a big box that can’t save your work when the battery is missing. You want a plan and a battery.

H2: Where this product sits in the greater APC ecosystem
APC is known for a broad lineup of UPS devices, from desktop units to enterprise-grade solutions. The SRT line targets mid-sized deployments that need reliability and remote management without sacrificing form factor. The NC variant fits a common pattern in which you buy the skeleton first and fill the bones with the power you deem necessary. If you already own an APC ecosystem, you can often leverage the same management tools and software to monitor your entire rack, which is convenient when you’re juggling a dozen devices at once.

H2: A short, nerdy comparison with a familiar post
If you’re curious about how this stacks up against our other lab power posts, you might enjoy:
- A quick dive into UPS basics: <a href="{% post_url 2024-04-12-ups-101 %}">UPS 101: The Essentials</a>
- A post on choosing the right UPS for a lab: <a href="{% post_url 2025-07-01-lab-ups-choose %}">Choosing the Right UPS for Your Lab</a>

H2: Final verdict: should you buy the APC SRT1000RMXLA-NC without a battery? So, yes, if...
- You’re a lab owner who wants a modular approach and is comfortable with a two-part purchase.
- You value clean, reliable power management and want to invest in a system that can scale with your rack without being a dead-end unit.
- You’re prepared to pick and purchase a compatible battery pack to achieve the runtime you need.
- You enjoy the satisfaction of building a powered lab from the ground up, battery by battery, literally.

If any of the above describes you, the SRT1000RMXLA-NC is a strong base platform. It’s not a “plug it in and run forever” device, but it is a capable, rack-ready UPS that can be tuned to your exact needs with a battery pack, software integration, and a thoughtful shutdown policy. And if you’re shopping around, consider how future-proof you want your rig to be: a compact, modular unit with a healthy ecosystem of accessories tends to age better than a boxed single-solution product, especially in a nerdy environment where upgrades are practically a hobby.

H2: Quick tips for getting the most out of your SRT1000RMXLA-NC
- Budget and plan for a battery pack that matches your expected runtime at your usual load. Do the math and run a few trial outages to see how long you’ll actually be powered.
- Enable safe shutdown policies across critical hosts. This protects data and saves your lab’s reputation as the place where no one loses work to a blackout.
- Utilize PowerChute or your preferred monitoring stack to receive alerts when the UPS is nearing capacity or when it needs service. Monitoring is a superpower, almost as cool as your personal coffee mug that reads I power stuff in the lab.
- Regularly test the UPS with maintenance testing and battery tests (per APC guidelines). It’s not fun to do, but it’s less fun to discover during a storm that your batteries are on vacation.
- Keep an eye on battery replacement cycles and inventory a spare. You don’t want to be the hero who improvises a battery from a random 9-volt cell and a prayer.

H2: Summary in a single nerdy line
APC SRT1000RMXLA-NC is a capable, rack-friendly UPS platform that shines when you treat it as a modular system: install the shell, pick and install the battery pack with care, configure the software, and enjoy clean power and safe shutdowns for your lab experiments and late-night code marathons. It won’t do your job for you, but it will make sure your job doesn’t vanish when the lights do a dramatic unplugging of the stage lights.

H2: Final recommendation
- If you’re building a lab from scratch and want a scalable, modular UPS with a solid feature set and strong support behind it, the SRT1000RMXLA-NC is a sensible choice—provided you budget for the battery pack up front and set up a sensible runtime expectation.
- If you need immediate runtime and you don’t want to chase a separate battery pack, consider alternatives that include a battery module in the box. Depending on your workflow, those might offer you faster time-to-value.
- If you’re already a loyal APC user with a ready-to-go battery pack, this NC edition can slot into your existing ecosystem without much friction and give you more capacity to protect your lab assets.

Internal links to related Geeknite posts for context and deeper dives:
- UPS 101: The Essentials — <a href="{% post_url 2024-04-12-ups-101 %}">UPS 101</a>
- Lab Ups and Strategy — <a href="{% post_url 2025-02-01-lab-ups-strategy %}">Lab UPS Strategy</a>

External resources for deeper understanding:
- APC official SRT Series page: https://www.apc.com/us/en/products/smart-ups-srt-series/
- General power management: https://www.geeknite.example/power-management

The bottom line: If you crave modularity, control, and clean power for a modern lab, the APC SRT1000RMXLA-NC deserves a serious look—just don’t forget the heart before you feed it the blood of electrons: the battery.

**Buy now through our affiliate link and support the nerdy cause: https://affiliate.geeknite.example/apc-srt1000rmxla-nc**