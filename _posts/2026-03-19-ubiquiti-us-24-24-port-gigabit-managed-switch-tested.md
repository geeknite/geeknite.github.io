---
title: Ubiquiti UniFi US-24: 24-Port Gigabit Managed Switch Tested (NOT PoE)
date: 2026-03-19
tags:
  - Networking
  - Ubiquiti
  - UniFi
  - Switch
  - TechReview
  - Geeknite
---

![Ubiquiti UniFi US-24 in rack]({{ '/assets/images/ubiquiti-us-24-in-rack.jpg' | relative_url }})

Introduction
------------
Welcome to Geeknite’s deep dive into the Ubiquiti UniFi US-24, the 24 port gigabit managed switch that refuses to power PoE devices on principle. If you are building a small to medium office network and you want a solid, unapologetically boring piece of hardware that just gets the job done, the US-24 is probably in your shopping cart right now. It is the quiet workhorse that makes your routers jealous of its calm, cable-managed aura. In this review we will push it through the paces, talk about setup, performance, quirks, and whether this switch deserves a place in your nerdy heart and your network rack.

What is the UniFi US-24?
-----------------------
The UniFi US-24 is a 24-port gigabit managed switch from Ubiquiti’s UniFi line. It is designed to sit in a standard 19-inch equipment rack and be the backbone of a small office or SMB network. Important detail for this review: this particular model is NOT PoE capable. If you need to power IP phones, cameras, or access points directly from the switch, you’ll want a PoE-capable model like the US-24-250W or similar. The US-24 is all about delivering reliable, predictable switching, VLANs, QoS, and the stability of the UniFi Controller ecosystem without the extra PoE drama.

Unboxing and hardware impressions
---------------------------------
The US-24 arrives in a clean, no-nonsense box that communicates purpose over flair. You get the switch itself, a rack mount kit, a couple of rack ears, a power cord, and a manual that you’ll probably skim for the “how to reset” page and then bookmark the rest for later. The chassis is a sturdy 1U metal beast with a matte black finish that makes your desk look vaguely like a data center after a few beers. The front panel is clean: 24 RJ45 ports in ascending order from left to right, with color-coded status LEDs per port. On the back, you’ll find the power input and two small fans that do their best impression of a humming kettle when you push the switch to full tilt during a lab test.

The physical spec highlights you should care about
---------------------------------------------------
- 24 x 10/100/1000 RJ45 ports, non-PoE
- 2 x SFP ports for fiber uplinks or stacking options (depending on firmware and model)
- Layer 2 switching with VLAN support, basic QoS, and link aggregation
- Non-blocking performance in a small business environment (your mileage may vary in a lab with a wind tunnel)
- UniFi Controller managed, meaning you get a single pane of glass for configuration across your UniFi devices
- Fan noise: present but acceptable in most office environments; in a quiet home office you’ll notice it if the device is within arm’s reach

Setup and getting started
-------------------------
If you have ever set up a UniFi AP or a UniFi Security Gateway, you’ll feel at home here. The US-24 plugs into your network, you connect to it via its IP on the LAN, and then you adopt it through the UniFi Controller. The Controller acts like a benevolent conductor, telling each device when to play nice and when to stop trying to synchronize with the neighbor’s lights (which is to say, VLANs, access control lists, and QoS rules). If you’re new to UniFi, the Controller is the central nerve system that makes sense of all your devices instead of pretending to be a free-floating cluster of gadgets with their own tiny universes.

Adoption workflow in the Lab
-----------------------------
- Power on the US-24 and connect it to your network.
- In the UniFi Controller, choose Devices and Add New. The US-24 should appear as an unadopted device.
- Click Adopt and wait for the green checkmark. If you have two-factor, you’ll confirm the device as part of your growing network empire.
- Create a basic switch profile in the Controller: VLANs for guest networks, a management VLAN, and a default untagged port for your lab laptop.

Internal architecture and what you feel when you poke around
------------------------------------------------------------
The US-24 uses a standard layer 2 switching fabric with a typical non-blocking path for ordinary home and small office traffic. In practice, this means your file transfers across the 24 ports don’t instantly become a digital charity drive for your router’s CPU. The performance is more than enough for everyday tasks like transferring large files between machines, streaming local backups, and playing LAN party in a small conference room style setting without resorting to macro-level network gymnastics.

Performance and real-world testing
-----------------------------------
Let’s talk about what you can actually expect from the US-24 in a real environment. We tested with several common office scenarios: file copying between NAS shares, media streaming between client devices, VoIP traffic on a separate VLAN, and uplink performance to a primary router topology. Here are the takeaways from our tests:

- Latency under normal load remains minimal. If you’re pushing 1 Gbps streams across multiple ports, you’ll observe latencies that are well within acceptable ranges for general office tasks. The switch isn’t designed to be a gaming router replacement, but it handles the occasional latency spike with surprising grace.
- QoS rules behave as expected. When you assign higher priority to voice traffic or critical server ports, the controller enforces it. In practical terms, this means VoIP calls stay crisp when someone in the office streams a movie or runs a backup.
- VLAN isolation works like a charm. You can segment networks for guests, contractors, or IoT devices without adding another firewall appliance. The experience is consistent with other UniFi devices, which means you can extend your firewall policies across the whole campus with minimal drama.
- Uplink options via SFP ports provide flexibility. If you’re in a scenario where you want to run fiber to the core or you’re stacking multiple switches with LACP, the two SFP ports offer a reasonable expansion path without needing extra hardware. Do keep in mind that SFP modules and DACs may vary in price, so plan accordingly.
- Power and heat: the unit stays relatively cool under lighter loads. Under sustained full-port activity, you’ll notice the fans doing their best to maintain a reasonable temperature, but it’s still within comfortable office noise levels.

A note on PoE and why this model is NOT PoE
-------------------------------------------
Because this is a non-PoE switch, you cannot power PoE devices directly from its ports. If you plan to deploy IP cameras, POE phones, or wireless APs, you’ll either need PoE-capable switches in the same network or a PoE injector per device. This is a conscious design decision by Ubiquiti for this model: it focuses on reliable switching and management rather than powering devices. If you want a single device that acts as both switch and power supply, you’ll want to look at models like US-24-250W or similar.

Feature set and what it means for your network
------------------------------------------------
- VLANs: The US-24 supports VLAN tagging on ports, enabling you to isolate traffic for security and performance. Great for separating guest networks from internal resources and ensuring your payroll data doesn’t wander into the break room.
- Link aggregation (LACP): You can bond multiple ports to increase uplink capacity to your router or a core switch. This is particularly useful if you’re streaming backups to a NAS on a separate path or if you’re running a high-lidelity lab environment where multiple machines pull data from a central server.
- QoS: Quality of Service rules give you control over which traffic gets priority. If your VoIP phone is on a separate VLAN, you can make sure the call quality remains pristine even when backups are happening in the background.
- Management: The UniFi Controller centralizes configuration, updates, and monitoring. It’s the same vibe you get from other UniFi devices, so if you’re already invested in the ecosystem, you’ll feel right at home.

Cable management and rack mounting
----------------------------------
If you’re a perfectionist about your rack aesthetics, you’ll appreciate the US-24’s slim 1U form factor. The included rack ears make mounting a breeze, and the device’s dimensions fit neatly into most standard 19-inch racks. The front panel LEDs are bright enough to be legible in a moderately lit office environment, but not so bright that they cause insomnia for the network admin who stares at them all night during a firmware update. If you want to label ports for simpler troubleshooting, consider pairing the switch with color-coded cables and write-on cable tags—your future self will thank you when you’re tracing a misrouted VLAN at 2 AM.

Comparisons and alternatives
-----------------------------
If you’re shopping within the UniFi ecosystem, you’ll likely compare the US-24 to the PoE variants and to other brands that offer similar 24-port switches. Here are a few quick thoughts:
- PoE variants: If your goal is to power access points and cameras directly, consider UL 24 PoE variants. They simplify cabling and reduce the number of power adapters in your rack, at the cost of heat, price, and a slightly more complex power budget planning exercise.
- Non-UniFi switches: There are perfectly capable non-UniFi switches from other vendors. The upside is potentially lower cost, but you’ll sacrifice the same central management experience. If you crave a single pane of glass for your entire network, UniFi remains the strongest argument in its category.
- Rack density and noise: The US-24 sits at a reasonable noise level for many offices. If you absolutely must have near-silent operation in a home office, consider placing it in a closet or cabinet with ventilation. The alternative is a different brand with a more aggressive cooling profile—but then you might be exchanging noise for slightly different software quirks.

How this switch fits into a modern home or small business network
----------------------------------------------------------------
The US-24 is at its sweet spot when you need a robust, centrally managed switching core for a growing office that doesn’t yet demand PoE power on every device. If your network has multiple VLANs, a few cloud-managed devices, and a desire to scale without losing control, this switch is a compelling option. It is not flashy, nor does it pretend to be a Swiss Army knife of features. It’s a dependable clamp that helps you keep cables organized, traffic predictable, and access control consistent across devices.

Cross-linking to our other guides
---------------------------------
If you’re building a more comprehensive UniFi environment, you may want to explore:
- VLAN basics for small offices and how to structure your networks for guest access and IoT isolation. See our post on VLAN basics: {% post_url 2025-01-15-vlan-basics %}
- Cable management strategies to keep your rack tidy and maintainable. Check our guide here: {% post_url 2024-11-11-cable-management-101 %}
- A primer on UniFi Controller topologies and why centralization matters for firmware updates and policy enforcement. We’ve got a broader piece on controller design patterns you may enjoy.

External references and product pages
--------------------------------------
- Ubiquiti UniFi US-24 product page: https://store.ui.com/products/unifi-switch-us-24
- Ubiquiti official documentation on VLANs and switching: https://help.ui.com/hc/en-us/sections/115000625809-UniFi-Switches

Pros and cons at a glance
--------------------------
- Pros:
  - Solid port density with 24 ports for a growing small office
  - Clean UniFi Controller integration for consistent management
  - VLAN and QoS features that are practical in real-world networks
  - SFP uplink options for flexible topologies
- Cons:
  - Not PoE, so you’ll need additional PoE infrastructure for powered devices
  - Not a game-changing feature set; it’s a workhorse, not a showhorse
  - Fan noise can be noticeable in a very quiet home office

Verdict and final recommendation
--------------------------------
If you are building or expanding a small to mid-size network and you want a reliable, manageable switch that won’t surprise you with power quirks or odd firmware behavior, the UniFi US-24 is a strong candidate. It excels in stability and ease of use within the UniFi ecosystem, offering straightforward VLANs, sensible QoS controls, and the reassurance that your core switching hardware won’t derail your entire office workflow during a firmware update. It’s not the cheapest option in the class, but the value comes in the form of predictable performance and a single management framework that scales with your other UniFi devices.

Who should buy this switch
----------------------------
- Small businesses that already rely on UniFi gear or plan to build a UniFi network across multiple rooms
- IT admins who want a centralized, controller-based approach with predictable configuration across devices
- Home labs where power over Ethernet isn’t required, but robust, manageable switching is desirable

Who should look elsewhere
---------------------------
- If you need PoE on every port or want an all-in-one PoE switch for cameras and access points, a PoE variant would be more appropriate
- If you’re on a tight budget and don’t mind managing devices individually, some non-Unifi switches may offer better price-per-port values
- If you want silent operation in a dedicated home office, you may want to place the switch in a closet or under a desk away from the main working area

Final thoughts
--------------
The US-24 is less about flashiness and more about delivering a dependable, well-integrated network core for the UniFi ecosystem. It’s the kind of device that makes you feel like a responsible network adult: you set it up, you configure VLANs, you assign QoS, you monitor uptime, and you sleep at night knowing the data you care about is traversing a controlled, predictable path. If your Ethernet dreams involve a setup that’s easy to manage and scalable, the US-24 is a solid foundation.

Final recommendation summary
----------------------------
- Core use case: SMB or home office with UniFi devices needing a robust, centrally managed switch
- PoE requirements: none on this model; plan PoE separately for powered devices
- Manageability: excellent with UniFi Controller; quick adoption and consistent policy application
- Future-proofing: reasonable, with SFP uplinks and VLAN/QoS features that keep you on the right side of network hygiene

Affiliate note and purchase prompt
----------------------------------
If you’re convinced this is the right core switch for your network and you’re ready to lock in a setup that won’t quit on you after 18 months, consider grabbing it via our affiliate partner. You’ll support Geeknite while getting a product that has earned its keep in our lab.

**Buy the Ubiquiti UniFi US-24 now through our affiliate link and power your network with the calm efficiency of a librarian who loves cables.** https://store.ui.com/products/unifi-switch-us-24

Would I buy it again? Yes. It’s not flashy, but it’s dependable, and for many real-world small business scenarios, that’s exactly what you need. If you want PoE, plan around a PoE-capable sibling in the family, and you’ll have a complete stack that’s easy to manage through the UniFi Controller.

Related posts you might enjoy:
- See VLAN basics in our guide: {% post_url 2025-01-15-vlan-basics %}
- Cable management 101 for tech desks: {% post_url 2024-11-11-cable-management-101 %}
- If you’re curious about mixing PoE devices with non-PoE switches, check out our feature on network expansion strategies with UniFi devices.

External links
--------------
- Ubiquiti official UniFi Switch US-24 product page: https://store.ui.com/products/unifi-switch-us-24
- UniFi help center on VLANs and switching: https://help.ui.com/hc/en-us/sections/115000625809-UniFi-Switches

Thanks for reading Geeknite’s practical take on the US-24. If you enjoyed this deep dive, keep an eye out for more hands-on hardware explorations with a dash of sarcasm and a lot of love for tidy cables.

Bold call-to-action for our readers
-----------------------------------
**Click here to grab the US-24 through our trusted affiliate and support Geeknite at the same time: https://store.ui.com/products/unifi-switch-us-24**