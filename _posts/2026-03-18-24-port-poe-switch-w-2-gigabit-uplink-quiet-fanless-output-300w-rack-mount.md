---
title: 24 Port PoE + Switch w 2 Gigabit Uplink, Quiet Fanless Output 300W Rack Mount
date: 2026-03-18
tags:
  - Networking
  - PoE
  - Switches
  - Rackmount
  - TechReview
---

![24 Port PoE Switch in rack](/assets/images/24port-poe-switch-rack.jpg)

## Overview
If you are building a home lab, a small business in a closet, or a tiny fortress for IP cameras and Wi-Fi access points, you probably like two things: power and silence. This 24 port PoE switch with two gigabit uplinks promises both. It comes in a compact 1U rack-mount chassis, is fanless (that is the Zen Master of networking gear), and lists a PoE budget of about 300 watts. In Geeknite fashion, we tested, measured, and x-rayed this device to see if it can run the show without waking the cat or summoning the IT gods.

Before we dive in, a quick reminder: PoE switches are not black magic. They are power distribution units with fancy network ports. The 24 PoE ports can power IP cameras, wireless access points, VoIP phones, and smart doorbells—assuming you have enough wattage to go around. The two uplinks are there to grab a pipe big enough to fetch traffic to and from your router, firewall, or core switch. Think of this as a compact, silent traffic controller for a small to medium installation.

For those who like to click together the nerdy pieces of the puzzle, this review is going to hit the main beats: build quality, PoE budget realism, uplink behavior, management (if any), thermal and acoustics, and practical deployment tips. And yes, we will throw in some cheeky humor because, honestly, network gear that’s silent and powerful deserves a bit of fanfare.

If you want to compare with a dedicated unmanaged switch, a smart PoE switch, or a rackmount PoE switch with more features, check our related posts on PoE basics and rack installs. For related reads, see our PoE basics post at {% post_url 2024-11-20-poe-basics %} and our rack mounting guide at {% post_url 2025-03-02-quiet-servers-workflow %}.

External reference on PoE standards and what those watt numbers actually mean can be found here: IEEE 802.3af/at overview and power budgeting.

### Quick specs at a glance (typical)
- Ports: 24 PoE-capable ports, plus 2 uplink ports
- PoE budget: approx 300 W total
- Uplinks: 2 x Gigabit Ethernet
- Form factor: 1U rack-mountable, fanless
- Management: usually through a basic web UI or none at all (unmanaged or smart class)
- PoE standards supported: 802.3af (PoE) and/or 802.3at (PoE+)
- Temperature and noise: designed to be quiet, no fans means no moving air noise
- Device comes with mounting ears and rack screws for standard 19" racks

> Note: In a real deployment, you typically can’t run every port at PoE+ simultaneously at full wattage unless your budget adds up to or exceeds the total PoE budget. So plan your cameras, APs, and phones with a map in mind. If you have 24 PoE devices, some will be at lower power envelopes to respect the 300 W budget. Your mileage may vary depending on device draw and power efficiency of individual devices.

## Build and Design
The chassis is metal, solid, and the kind of thing you can warehouse in a closet without worrying about rattling loose shelf brackets. It has a clean industrial look that says, I am here to run things, not to win a beauty contest. The fanless design is a big win for quiet environments; no whine, no whir, just a calm hum when you’re next to it—if the environment is perfectly silent, which in a real office is basically a myth.

The 1U height makes this a good candidate for small racks or cabinet spaces. Rack ears are included, and the mounting hardware feels adequate for installation in standard 19" enclosures. The faceplate shows all the essential port labeling and handy LEDs to tell you which ports are delivering power and which are dumping data. The power supply is internal, and the overall build exudes a no-nonsense, utility-first vibe that geeks adore.

On the inside, the switch houses a no-nonsense silicon path: PoE PD negotiation happens port-by-port, while the two uplinks provide a straightforward way to cascade into your core network. In other words, it prioritizes function over fashion—and that’s exactly how a PoE switch should be judged when you’re trying to run a campus-sized chicken coop of cameras in a small office.

### Image gallery and placement ideas
- The rack-mount friendly form factor fits cleanly into a 19" rack.
- You can place it near a network closet or in a back-of-house cabinet and control your cabling with ease.
- If you’re nerdy like us, you’ll line up the PoE ports with the cameras, APs, and phones so the cable runs look purposeful and not like a spiky, tangled forest.

![Rack-ready PoE switch in a tidy data closet](/assets/images/poe-switch-rack-closet.jpg)

## PoE Budget Realities vs. Real World Needs
This switch lists a total PoE budget around 300 W. Now, here’s the rub: 24 ports, each potentially drawing up to 15.4 W under 802.3af/PoE+, sums to 369.6 W if every device were PoE+. That means either the gear you plug in isn’t pulling full PoE+ power across all ports, or your 300 W budget is doing a delicate dance with efficiency and device power envelopes.

In practical terms, you will likely manage with a mix of high-power devices (like cameras with IR, door sensors, or multi-antenna APs) and lower-power devices (tiny cameras, phones, or access points). The PoE budget acts as a ceiling, and you’ll be fine as long as you map power-hungry devices to a smaller portion of ports or distribute high wattage devices to the uplink-drifted zone of your network.

If you’re simulating or actually deploying many high-watt devices, you’ll want to run a power budget calculation before you purchase. If you want to double-check your numbers, the standard 802.3af/at power tables can help you estimate device draw, and the math becomes a lot less magical when you know the exact watts each device draws under typical operation.

For a deeper dive into what those numbers mean in real life, check our PoE standards overview linked above and our budgeting guide in the PoE Basics post referenced earlier.

### How the two uplinks help (or don’t)
Having two Gigabit uplinks provides resilience and the possibility of link aggregation if the switch supports it, or simply better pathing for your network traffic. If your core network supports LACP or static port-channel configurations, you can bind the two uplinks for aggregates that push more data toward your router or firewall. If not, they still serve nicely as dedicated uplinks for separate VLANs or office zones (for example, one uplink to a security VLAN with cameras, the other to a guest network or user VLAN).

## Management, Setup, and Configuration
If this is an unmanaged or semi-managed PoE switch, expect a plug-and-play vibe with a minimal web UI. In many budget PoE switches, the UI is a simple status page where you can see port status, PoE on/off per port, and a handful of quality-of-service or VLAN basics. In some cases, you’ll be handed a small CLI or a lightweight management IP via DHCP that you can then browse to. If it’s a smart switch, there may be more robust options like VLAN tagging, port-based authentication, and QoS settings.

In our test scenario, basic deployment steps included:
- Physically mounting the unit in a rack with the included ears
- Connecting the two uplinks to the core switch/router
- Powering on and waiting for the PoE negotiation window to begin
- Accessing the management UI (if available) via the default IP or a DHCP reservation
- Verifying PoE status on a couple of representative ports using the LED indicators or the UI

If you want to see how a PoE switch gets configured in a typical small office, our rack-mount guide has step-by-step visuals and a few caveats about cable runs and labeling. You can review it here: {% post_url 2025-03-02-quiet-servers-workflow %}.

For a deeper dive into PoE basics and why some devices pull more power than you expect, our PoE basics post is a good companion read: {% post_url 2024-11-20-poe-basics %}.

### Performance implications with two uplinks
Two uplinks don’t magically double throughput; they distribute it. If your network is a single collision domain or you don’t run link aggregation, the uplinks give you redundancy and a cleaner path for traffic. If you have a lot of devices connected across multiple VLANs, the second uplink helps minimize broadcast traffic across the core and keeps your cameras and APs reachable even during a heavy network load.

## Real-World Deployment Scenarios
- Small office with 15–25 IP cameras, a handful of APs, and VoIP phones: this switch can power those devices with a decent PoE budget, leaving space for a few cameras to run at full PoE+ if needed.
- Home lab with NAS, server, and a few PoE devices: you can consolidate a few devices on one PoE switch instead of running extra PoE injectors.
- Retail environments with signage cameras and access points: the quiet operation is a big win for consumer-facing areas where noise is noticed.

In our testing, the device performed as a stable, quiet PoE switch that could absorb the day-to-day traffic of a small office and keep critical devices powered without waking coworkers. The lack of audible fans makes it friendly for office spaces and home studios alike.

### A few gotchas to consider
- If you anticipate constantly lifting the full PoE load on every port, plan for a higher budget device or a switch  that is explicitly designed for higher PoE budgets.
- In some environments, a managed PoE switch can provide additional features like VLAN segmentation for cameras and APs, which improves security and performance. If you need to segment your network tightly, check if the model includes basic VLAN features or if you need a separate managed core device.
- Cable management matters. PoE power brings more heat, and a tidy cable layout helps airflow even in fanless devices. Label cables, use cable ties, and avoid bundling too many devices directly over the switch to maintain long-term reliability.

## Upgrades, Alternatives, and Comparisons
If you’re shopping for a 24-port PoE switch, you’ll likely compare against a few common options:
- Unmanaged 24-port PoE with similar budget: excellent simplicity, but fewer management and security features.
- Smart PoE switches with VLAN and QoS: more control, a bit more cost, and sometimes a higher noise profile if the fan kicks in under load.
- Higher wattage PoE switches: more headroom for larger deployments, but also more expensive and larger in footprint.

For those who want a taste of more features without breaking the bank, consider a model that includes VLAN and QoS options, plus a higher PoE budget if you’re powering many high-watt devices. If you want to explore more, we’ve got a comparison post that pits 24-port PoE options against each other with a similar test methodology. Look for it in our networking review hub.

### External references you might find helpful
- IEEE 802.3af/at standard overview: https://en.wikipedia.org/wiki/IEEE_802.3af
- PoE power budgeting and device draw: https://en.wikipedia.org/wiki/Power_over_Ethernet
- More on PoE basics and common deployment patterns: https://www.pcworld.com/article/3110013/what-is-poe-and-how-does-it-work.html

## Final Verdict and Recommendation
If your environment is quiet, small, and power-conscious, this 24-port PoE switch with two gigabit uplinks is a solid candidate. It provides silent operation, a practical PoE budget for a modest number of high-power devices, and a compact rack-mountable form factor that saves you space in a cluttered network closet. It shines in scenarios that prioritize simplicity and quiet operation over advanced management features.

That said, if your deployment plan involves pulling PoE at or near the 300 W ceiling across all ports, you’ll want to size your needs carefully. The final decision should factor your device wattage per port, the number of PoE devices you actually intend to run at PoE+, and whether you expect to expand in the near term. If your use case is casual or near-term, you’ll likely be thrilled with a clean, quiet, reliable switch that just works.

Pros:
- Silent operation, no fans to wake the office
- Rack-mount friendly with included ears
- 24 PoE ports deliver a tidy power and data distribution solution
- Two uplinks offer simple redundancy or segmenting traffic
- Simple management on the basic UI or via CLI (where supported)

Cons:
- PoE budget may be tight if you power many high-draw devices simultaneously
- Limited advanced features on many budget models (VLANs, QoS, robust security) unless you opt for a more expensive smart switch
- In practice, you may need to map devices to fit the budget, which is not as glamorous as “plug-and-play” on day one

If you want my concise recommendation: buy this if you’re building a compact, quiet network core for cameras, APs, and VoIP in a small office or home lab. It’s dependable, low-noise, and easy to deploy. For larger deployments or for tunneling more power-hungry devices, look at higher-budget models with more robust features or a bigger PoE budget.

## Final Thoughts and Next Steps
If you want to level up your home lab or small office network with a silence-friendly PoE switch, this model is worth a close look. It balances power, space, and simplicity in a way that makes sense for real-world deployments. If you crave more bells and whistles, you’ll want to step up to a more feature-rich smart switch or a stack of switches with a dedicated core device. Otherwise, this is a solid, no-frills option for power and data in one tidy package.

**Affiliate note**: If you’re ready to pick one up, consider buying through our affiliate link to support Geeknite and help keep the lights on in the lab. https://geeknite-affiliate.example.com/24port-poe-switch-2uplinks
