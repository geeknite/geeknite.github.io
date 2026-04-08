---
title: Ubiquiti UniFi US-24: 24-Port Gigabit Managed Switch Tested (NOT POE)
date: 2026-04-08
tags: [gear, networking, uniFi, review, geeknite]
---

# Ubiquiti UniFi US-24: 24-Port Gigabit Managed Switch Tested (NOT POE)

![Ubiquiti UniFi US-24 front panel](assets/images/ubiquiti-us-24-front.jpg)

If you're the kind of person who treats a switch like a puzzle box to be solved while humming the theme to a sci-fi show, the UniFi US-24 is probably right up your alley. It’s a 24-port, non-PoE, managed switch that sits in the middle of the UniFi lineup: not as compact as the little US-8-150W, not as feature-snooty as the giant Enterprise switches, and definitely not as sassy as the Dream Machine line. In short: it’s the practical, room-temperature condiment of the UniFi ecosystem—deliciously reliable, not glamorous, and absolutely necessary if you want your network to function without drama.

![Rear panel with two SFP ports](assets/images/ubiquiti-us-24-rear.jpg)

This review takes you through setup, performance, and why you might actually want a non-PoE 24-port switch in a home or small-office lab. Spoiler: PoE is not this guy’s jam, but there are a lot of reasons you’d still want to opt for a US-24 over a PoE model if you’re not feeding powered devices directly from this switch.

If you’re hunting for the official spec sheet before we dive in, you can peek at Ubiquiti’s product page here: https://store.ui.com/products/unifi-us-24. And if you want to nerd out on the architecture behind UniFi switches in general, the UniFi Switch documentation is a treasure trove: https://help.ui.com/hc/en-us/sections/115000959047-UniFi-Switch. For a contrasting perspective, you might enjoy our write-up on the Dream Machine and how it interacts with standard unmanaged gear in {% post_url 2025-03-12-geeknite-setup-dream-machine-review %}.

---

## Introduction: Why a 24-Port Non-PoE Switch?

Networking gear tends to fall into two camps: the “I must power all the things” PoE crowd and the “I just need fast, stable switching with decent management” folks. The UniFi US-24 sits squarely in the latter camp. It’s not meant to deliver power to APs, cameras, or IP phones; it expects you to handle PoE devices upstream or with separate PoE injectors/switches. This separation can actually be a blessing in disguise because it keeps noise and heat from PoE-driven devices away from your core switching fabric, and it tends to be a cheaper option for labs and small offices that already have power budgeting under control.

From a design standpoint, the US-24 is a classic UniFi device: sturdy metal chassis, fan(s) that are there for cooling rather than style, and a web/Controller interface that makes you feel like you’re piloting the USS Enterprise while just transferring packets. It’s a workhorse rather than a showhorse, which fits Geeknite’s philosophy: performance plus a little whimsy, but mostly utility.

For the price of a couple of fancy coffee runs, you can tuck this switch into a rack and forget it exists—until you realize you can finally get 1 Gbps to every desktop in a 20-seat office without the network creaking under the pressure. In many homes or small offices, the question isn’t “do I need a 24-port switch?” but “which 24-port switch should I pick that won’t spontaneously become a fan-powered space heater?” The US-24 answers with quiet competence.

---

## Package, Build, and First Impressions

The packaging is typical UniFi: clean, no-nonsense, and not trying to upsell you with jargon you don’t understand. Inside you’ll find the switch, an AC power cord, a handful of rack ears if you want to mount it, a small manual, and a basic Ethernet cable for initial testing. Realistically, you’ll replace that cable within five minutes with something you care about, but it’s there when you’re unboxing at 2 a.m. and your cat is judging your life choices.

In terms of build quality, the US-24 is heavy enough to feel substantial but not ridiculous. It’s a metal chassis with a front panel that bears the familiar LED array for port activity, along with a couple of status indicators. The two SFP ports on the rear provide fiber or copper uplinks, which is a nice touch for future-proofing an edge network or a small data center corner without needing a separate 10G switch. The fans—if present in your unit—are optimized for cooling instead of being a loud badge of honor. If you’re building a quiet home lab, you’ll notice the switch operates with a soft whir rather than a jet engine, which is exactly what you want during late-night tinkering sessions.

Setup is where UniFi shines for the right audience. You don’t configure the US-24 with a CLI, unless you’re a masochist who loves typing commands into a glowing terminal while your coffee goes cold. Instead, you adopt the switch via the UniFi Network Controller (or UniFi OS if you’re running a Dream Machine/Newer Cloud Key). The process is straightforward: plug it in, adopt in the controller, assign VLANs if needed, create your trunk ports, and you’re done. The controller handles firmware updates automatically (with the caveat that you should schedule them during non-peak hours if you’re in a business environment).

For the curious, the US-24’s default configuration is clean and sensible. If you’ve used UniFi gear before, you’ll feel right at home. If you’re new to UniFi, you’ll be guided by the same clean UI that makes most people think, “ coordinating networks with a single pane of glass sounds almost magical.” And it kind of is, until you realize you spent three hours customizing an NTP time server and forgot why you started.

---

## Hardware Specs and What They Mean for Us

The US-24 is a 24-port switch with 24 Gigabit Ethernet ports and 2 SFP uplink ports. It’s designed for simplicity, reliability, and centralized management. It doesn’t attempt to do more than that, which is a luxury many busy offices forget they want until an upgrade is long overdue. Here are the highlights you’ll actually care about in the field:

- 24x 1 Gbps RJ45 ports for devices like desktops, printers, NAS, and non-PoE APs or cameras routed through PoE switches elsewhere in the stack.
- 2x SFP ports for fiber or copper uplinks, enabling you to stitch together multiple switches or connect to a small core network without cannibalizing your 1 Gbps ports with uplink traffic.
- Layer 2 management features: VLANs, trunking, port isolation, Port-based ACLs, and robust MST/STP options to prevent loops in more complex topologies.
- QoS features that let you shape traffic to keep latency-sensitive applications happy, which is crucial if you’re running VoIP or a gaming PC in an office environment.
- CLI-lite comfort for power users, but the primary interaction remains through the UniFi Controller, which keeps things accessible for admins who would rather not memorize a command cheat sheet.
- Quiet operation with a reasonable cooling solution—great for a small rack in a shared space or an apartment lab.

In practice, these features translate into a “set it and forget it” experience. You can segment traffic, ensure that staff laptops don’t swamp your NAS backups, and keep your guests away from critical systems by locking down appropriate VLANs. If you’ve ever tried to juggle multiple routers and switches that don’t talk to each other, the US-24 and its UniFi ecosystem feel like a breath of fresh air: simple, cohesive, and a bit merciful to your sanity.

For those who like to compare, the key differentiator is the PoE capability. If you need to power access points, cameras, or IP phones from the same box, you’ll reach for a PoE-enabled model (or bring in an additional PoE switch). The US-24’s non-PoE status isn’t a bug; it’s a feature if your devices are already well-supplied with power or you prefer separating data and power management to simplify your power budget. It’s the engineering version of choosing to wear a wristwatch rather than a smart ring: not everything needs to be integrated, and sometimes simpler is better.

For a deeper dive into how UniFi handles VLANs and port-based policies, see {% post_url 2025-10-24-ug-uniFi-vlan-basics %} and {% post_url 2024-05-18-network-segmentation-101 %}.

---

## Performance Tests: How It Handles Real-Life Load

We put the US-24 through a slate of practical tests that mimic a small office and a home lab environment. The goal wasn’t to win a speed contest but to verify the switch’s behavior under realistic pressure: steady throughput, predictable latency, and reasonable CPU/memory headroom for the controller to do its thing without hiccups.

Test setup:
- A single uplink to a core router via one of the SFP ports, configured as a trunk with VLANs for management, user data, and voice.
- 20+ endpoints connected via the 24 RJ45 ports, including a NAS, a couple of workstations, and a desktop PC doing iPerf3 tests.
- A separate management workstation on a dedicated VLAN with firewall rules to simulate a typical office network.

What we observed:
- Latency stayed in a predictable range under moderate load, which is exactly what you want for voice and video calls going through your internal network.
- Throughput scaled nicely with the number of devices. It’s not a marketing poster child for busting 10 Gbps, but it doesn’t pretend to be. It’s meant to handle real-world traffic with stable performance.
- The controller’s interface remained responsive while monitoring traffic and making VLAN adjustments on the fly. If you have a big network, this is where UniFi starts feeling like a productivity tool rather than a hobby project.

We also tested PoE-separation-ish behavior by running a few PoE endpoints off a different PoE switch in the same VLAN as the US-24’s uplink. There was no cross-talk or weird behavior—something that matters when you’re stacking micro-systems in a small office and you don’t want the data plane to fight the power plane.

If you want to compare with other UniFi switches in real-world scenarios, our earlier post on a compact US-8 PoE and the all-in-one Dream Machine provide useful context: {% post_url 2025-06-11-compact-us8-poe-review %} and {% post_url 2025-08-02-unifi-all-in-one-review %}.

---

## Features Deep Dive: VLANs, QoS, and LACP

VLANs are the backbone of a sane network, and the US-24 handles them with confidence. You can create multiple VLANs, assign them to specific ports, and configure inter-VLAN routing via a routed gateway elsewhere in your network. For small offices, this means you can isolate guest Wi-Fi traffic from corporate resources, or keep IoT devices out of your critical data paths—without needing a sprinkler system to cool your brain during configuration.

QoS (Quality of Service) on the US-24 helps prioritize traffic. In a practical sense, that means you can ensure that a video call won’t be degraded by a sudden large file transfer from a NAS. It’s not magic, but it’s real-world helpful. You won’t get the same level of granular, application-level QoS as in enterprise-grade devices, but you’ll get enough to keep essential services stable without a headache.

LACP (Link Aggregation Control Protocol) support on the uplinks allows you to bond the two SFP ports (or combine RJ45 uplinks with SFP, depending on your hardware) for higher throughput and redundancy. If your ISP or internal traffic patterns require more than a single 1 Gbps path, LACP provides a straightforward path to higher aggregate bandwidth. It’s not a gimmick, it’s a smart way to plan for growth.

For the curious mind, here are some practical snippets you’ll use in daily operations:
- Creating VLANs for a guest network and a corporate network:
  - Guest: VLAN 20 with restricted access to corporate resources.
  - Corporate: VLAN 10 with full access to internal servers.
- Setting up a trunk on the uplink to carry multiple VLANs without dropping performance.
- Enabling Spanning Tree Protocol to prevent loops in a multi-switch environment.

If you want to cross-reference deeper, our VLAN basics post is a solid companion: {% post_url 2025-10-24-uniFi-vlan-basics %}.

---

## Ease of Use: Web UI, Controller, and Community Magic

The UniFi ecosystem is famous (or infamous, depending on how you look at it) for its single-pane-of-glass management. The US-24 plays nicely with the rest of the lineup, which means you can adopt the switch in the UniFi Network Controller, push configurations, and monitor it alongside your APs, cameras, and other switches. The learning curve is gentle if you’ve used UniFi before. If you’ve come from a world of vanilla web interfaces and mysterious CLI prompts, you’ll likely find the controller a refreshing change—organized, logical, and often pleasantly proactive about firmware updates.

For those who love a little humor in their lab notes, you’ll appreciate how the UI adds tiny touches: a whimsical green status light when everything is healthy, a gentle nudge if you misconfigure a VLAN, and a dashboard that makes you feel like you’ve actually got your network under control. It’s not “magic,” but it’s the kind of software polish that makes a difference in day-to-day administration.

If you’re new to UniFi, you’ll probably want to check out our getting-started guide first: {% post_url 2025-01-12-ubiquiti-setup-guide %}.

---

## Who Should Buy the US-24?

- Small offices or home labs that want a robust, non-PoE switch with good internal management and a straightforward upgrade path to a full UniFi stack.
- Environments where PoE devices are powered by separate switches or by PoE injectors elsewhere in the rack. This switch gives you the data plane stability and switch-level control without forcing you to deliver power through the same box.
- Networking enthusiasts who enjoy a clean, cohesive ecosystem and don’t want to wrestle with multiple vendor ecosystems for basic VLANs, QoS, and link aggregation.

Who should think twice:
- If you absolutely must power APs, cameras, or phones from the same device, consider a PoE-capable UniFi Switch model (e.g., US-24-250W) and use the US-24 as a non-PoE core switch in your design. The core idea is to match the product to your use case rather than forcing power through a switch that isn’t meant to deliver it.
- If you need 10G or faster uplinks in every port, you’ll want to look at newer or higher-end models with 10G/SFP+ or multi-GbE options. The US-24 shines in its domain, but it’s not a speed demon in a data-center sense.

For a broader look at UniFi stacking and how it can scale in a small business, you can skim our linked posts on multi-switch deployments and best practices: {% post_url 2025-05-30-small-office-networking-%} and {% post_url 2024-12-05-uniFi-stacking-guide %}.

---

## The Verdict: Should You Get It?

In Geeknite style: The UniFi US-24 is the reliable friend who shows up on time, does the job, and doesn’t complain about your cable spaghetti. It won’t win awards for flashiness, but it will keep your network stable, predictable, and easy to scale as your IT budget grows. If your network plan involves a few APs, a NAS, a handful of workstations, and a desire to keep management sane, the US-24 is a sensible choice that won’t surprise you with candy-coated features you’ll never use.

If you’re already in the UniFi ecosystem, the US-24 slots in as a perfect mid-range switch that can act as a core or distribution switch in a small office network. It pairs well with UniFi APs and cameras, and its two SFP uplinks give you a clear path to a small core without cluttering your floor with additional expensive hardware. In terms of build quality, software polish, and practical features, it’s a dependable workhorse rather than a flashy showpiece—and that’s exactly what many real-world networks need.

If you want a quick takeaway: non-PoE 24-port switches aren’t glamorous, but they’re incredibly useful when you’re building a clean, scalable, and maintainable network. The UniFi US-24 checks those boxes with a neat UI, solid performance, and a design that won’t get in your way when you’re trying to get a lot of devices onto your data plane.

For those who want a different flavor, check out our review of the PoE-capable cousin, the US-24-250W, to see where the power feature adds value (and where it adds extra management considerations): {% post_url 2025-02-18-ubiquiti-us-24-250w-review %}.

---

## Final Recommendations and Where to Buy

- Best for: Small offices or home labs needing a robust, non-PoE 24-port switch with UniFi management that won’t break the bank and won’t turn your rack into a space heater.
- Alternatives: If you need PoE on the same box, look at the US-24-250W or similar PoE-capable models in the UniFi lineup. If you’re aiming for higher speeds and more ports, you might step up to a USW-Pro or a more enterprise-grade UniFi switch with 10G uplinks.
- Setup path: Use the UniFi Network Controller to adopt, configure VLANs, and implement QoS. Keep your firmware up to date and monitor the device with the controller’s health dashboards.
- Final note: Don’t forget to pair this with appropriate PoE infrastructure if you plan to deploy UniFi APs and cameras at scale. The separation of data and power management can simplify troubleshooting and future upgrades.

If you’re ready to upgrade your network without breaking the bank, this is a strong candidate. It respects your time, respects your budget, and respects your need to actually have a functioning network that doesn’t require a degree in network engineering to manage.

---

### Related Reads
- Our deeper dive into VLANs and safe network segmentation: {% post_url 2025-10-15-uniFi-vlan-segmentation %}
- How to plan a small-business network with UniFi gear: {% post_url 2024-07-22-small-business-networking-uniFi %}
- A lab tour: setting up a home lab with UniFi switching and APs: {% post_url 2025-01-28-home-lab-uniFi-tour %}

**Final Recommendation: If you want a dependable, straightforward 24-port switch that plays well with UniFi devices and won’t overwhelm you with power demands, the US-24 is a solid pick. It’s not flashy; it’s effective.**

**Shop the UniFi US-24 now: https://affiliates.geeknite.example/uniFi-us-24**

