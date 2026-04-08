---
title: Ubiquiti UniFi US 24 24-Port Gigabit Managed Switch Tested Not PoE
date: 2026-04-08
tags:
  - Networking
  - UniFi
  - Hardware
  - Review
  - HomeLab
---

Intro

In the wild jungle of home labs and small offices, you want gear that just works without drama. The Ubiquiti UniFi US 24 is a 24 port gigabit managed switch that sits in the 1U rack space and does not power PoE devices. Our Geeknite lab gave it a proper beating to see if its quiet exterior hides a capable beast or just a pretty face with LED lights. If you want a clean network backbone that you can manage from a single pane of glass, this unit deserves a look. If you crave PoE for IP cameras and phones, you will want the PoE variants later in this review. For now, let us dive into a full take on the US 24 and whether it earns a place in your rack or simply collects dust bunnies.

![UniFi US 24 in rack]( /assets/img/unifi-us-24.jpg )

## Overview of the UniFi US 24

The UniFi US 24 is a 24 port gigabit switch designed for small offices and home labs. It is a non PoE model, so there is no PoE budget to speak of, which makes it incredibly simple for your non PoE devices. Its physical footprint is friendly to most 19 in racks and it sits neatly in 1U of rack space. The goal here is clarity and control rather than power delivery to connected devices. In our tests the absence of PoE means less heat and less fan noise, which translates to a quieter closet and happier engineers.

Key aspects we will cover include build quality, ease of setup, management capabilities, real world performance, and how the US 24 stacks up against PoE siblings in the UniFi family. We will also compare it to a few other switches in the same price class and talk about who should buy this model versus a PoE option or a smaller unmanaged switch.

## Unboxing and initial impressions

Opening the box reveals a clean, no nonsense packaging. You get the switch chassis, a pair of rack ears, a power cord, mounting screws for a standard rack, and a concise start guide. No mystery accessories here, just the essentials. The chassis is solid steel and the finish resists fingerprints and smudges better than that fancy smartphone you pretend to own. The attention to detail in the metalwork is typical UniFi: sturdy, functional, and designed to live in a climate controlled cabinet rather than under a coffee table.

In terms of physical design, the US 24 wears a minimalistic badge of silicon powered confidence. The front panel hosts 24 ports lined up in a neat row. LED indicators provide immediate status feedback for link up and activity. On the back you find the power input and the uplink options, which for the US 24 usually include a couple of SFP slots for fiber or copper fiber reach, depending on the exact revision. The unit ships with a standard rack installation kit and the width is friendly to most 19 in racks. In short, this is a device that looks like it belongs in the rack room with the rest of your network gear rather than a shelf in the living room.

For the photography lovers out there, here is a quick visual: ![UniFi US 24 in rack]( /assets/img/unifi-us-24.jpg )

## Setup and first configuration

Setup with UniFi gear is a pleasant experience when you approach it with a UniFi Network Controller in mind. The US 24 is designed to be adopted into a UniFi Network setup, which means you should have a Network Controller running on a dedicated machine or in the cloud. The workflow is designed to be intuitive for admins who hate manuals and love pretty dashboards.

1) Connect the switch to your management network and power it on. 2) Open the UniFi Network Controller and trigger the adoption workflow. 3) Once adopted, assign the device a friendly name and place it in the correct site if you have multiple sites configured. 4) Create port profiles and VLANs according to your network segmentation plan. 5) Optional: enable link aggregation if your uplink supports higher bandwidth or if you want to aggregate multiple uplinks for redundancy. 6) Save and watch the logs as the switch starts to populate its bridging tables and your VLANs become visible in the dashboard.

The key advantage here is not needing a CLI for routine tasks. The UniFi Controller handles configuration of VLANs, port isolation, QoS priorities, and LAGs via a clean, graphical interface. It is a joy for administrators who enjoy clicking their way through network policy rather than memorizing CLI commands. If you are coming from a non UniFi environment, the initial adoption might require a short learning curve as you align your older networks with UniFi’s model of device management. Still, the payoff is a single pane of glass for a whole suite of devices.

### Port configuration and VLANs

Port VLAN assignment is straightforward in the UniFi Network Controller. You can designate each port as access or trunk, tag VLANs appropriately, and apply port profiles so you can reuse the same configurations across multiple devices. The US 24 supports 802.1Q tagging and allows you to chain VLANs across multiple ports. For small offices especially, this is ideal for keeping devices like workstations on one VLAN while keeping printers, IP cameras, and guest devices on separate networks for security.

The ability to create and apply port profiles is a big time saver. You can create profiles for specific roles (PCs, printers, wireless access points) and apply them to the entire switch with a couple of clicks. In our lab, we found that once the require VLANs were in place, moving devices between ports or altering security policies happened in minutes rather than hours. The Unified Controller also makes it easy to create and apply QoS rules to ensure critical traffic like videoconferencing has priority while nonessential broadcasts take a back seat.

### SFP uplinks and LAG support

For the non PoE US 24, the SFP uplinks provide flexible options for fiber or copper connections to upstream switches or a small MDF. In our tests we used a pair of SFP uplinks configured in a LAG to a higher capacity core switch. The LAG feature behaved as expected, delivering a stable, aggregated uplink for multi-host traffic without odd renegotiations or jitter. If your environment requires more uplink bandwidth but you do not want to step up to a PoE capable switch, the US 24 with SFP uplinks is a compelling choice.

## Performance and testing in the Geeknite lab

Performance testing for a 24 port non PoE switch is mostly about how well it handles multiple simultaneous conversations. The US 24 is built for a robust Layer 2 switch role with a focus on reliability rather than raw PoE horsepower. In practice this means you can expect solid, predictable behavior when you have a lab full of laptops, servers, printers, and a handful of smart devices talking on VLANs.

### Test methodology

In our lab we set up a small topology with a few client VMs and a couple of dedicated test hosts. We configured VLANs for data, voice, and a separate management segment to mimic a real office. We used iperf3 for throughput tests and a few simple traffic generators to emulate mixed traffic across the 24 ports. The uplink was connected via SFP to a core switch that could act as a traffic sink, with a dedicated management network separate from the data VLANs to ensure that our tests did not interfere with administrative tasks.

We also tested typical home lab scenarios: file transfers between hosts on different VLANs, streaming video from a local server, and a handful of users performing web browsing while backup jobs run in the background. The aim was to push the switch through a realistic workload while keeping the configuration practical and maintainable.

### Results and observations

Overall, the US 24 performed as a solid Layer 2 device with stable performance under typical mixed workloads. A few takeaways from the lab:

- Line rate behavior: When a single large stream or multiple streams saturate the uplink toward the core, the switch maintains stable performance with minimal delay through the switch fabric. The per-port throughput remains in the expected 1 Gbps range for the majority of bursts, with overhead characteristic of real world operation.
- Aggregate throughput: With a well provisioned uplink (for example, a 2x1G or higher core uplink via LAG), aggregate throughput across several active ports remains strong without noticeable jitter or packet loss.
- VLANs and QoS: VLAN tagging works as described in the controller. QoS rules help ensure critical traffic such as voice or video conferencing has priority in congested scenarios. This is particularly valuable in small offices where a single bottleneck can ripple into many users' experiences.
- Latency: In our tests, switching latency remained low. For control plane traffic and real time services, the performance is more than adequate for small to medium sized environments. This is exactly what you want in a home lab or a tiny office where you need quick policy updates without surprises.

Anecdotally, we found that the lack of PoE on this unit reduces heat generation a bit, contributing to a quieter maintenance window. The absence of PoE reduces the power budget you need to consider for devices connected to the switch, which is a straightforward tradeoff to consider if you plan to deploy IP cameras or PoE devices on a larger network.

If you want to see how our results map to real world workloads, check out our earlier posts on network fundamentals and practice runs for small network builds. For context and deeper theory, see our post on basic network design and VLAN strategies, linked below via post URLs.

### Noise, power, and thermals

The US 24 keeps fan noise at a minimum. In a closet environment with reasonable airflow, the unit runs cool and quiet. There is no loud whine or buzzing at normal operating temperatures, which is a blessing for a home lab or a coworking space where noise can be a nuisance. Power consumption is modest compared to PoE switches with a large PoE budget. Since there is no PoE power draw, you do not need to factor PoE heat into your rack design. If you are building out a silent lab, this model is a strong candidate.

## Management UX and ongoing maintenance

The UniFi Network Controller is the central point of management for this switch. Once adopted, you can rely on the controller to push firmware updates, enforce port policies, and maintain a clear log of changes. In practice, the experience is not unlike managing a fleet of devices — a little learning curve if you are new to UniFi, but the payoff is a familiar, centralized interface for monitoring the entire network.

### Firmware updates

Firmware updates are straightforward: download the new version from the official portal, apply the update, and monitor the switch through the controller for any anomalies. In our lab, updates were smooth with minimal reboots and no unexpected service outages. The controller provides release notes, but you do not need to memorize every feature to benefit from the update. Install updates in a maintenance window if you are running a production environment to avoid unexpected traffic surges during the update window.

### Security and maintenance considerations

As with any manageable switch, keep the controller accessible only to trusted devices and VPNs. The UniFi ecosystem excels in visibility but does require administrative care to prevent misconfigurations. We recommend using a dedicated management VLAN or a separate admin subnet if you have external access to the controller. Enable two factor authentication on the controller to keep admin accounts secure. For a small office, this is a practical improvement that yields a safer, more predictable network experience.

## Pros and cons at a glance

Pros
- Quiet operation due to robust passive cooling and lack of PoE power draw
- Clean, rack friendly design with solid build quality
- Easy adoption via UniFi Network Controller
- Flexible port management with VLANs and QoS
- SFP uplinks enabling scalable uplink options

Cons
- No PoE means you need a separate PoE switch for powered devices
- Requires UniFi Network Controller for full feature set; not ideal for bare metal setups without controller access
- If you need high PoE budgets, you will need to consider PoE variants or larger PoE capable switches

## How it stacks up against PoE siblings

If you need PoE for cameras, phones, or wireless APs, UniFi offers several PoE capable switches. The non PoE US 24 is ideal when you want a strong Layer 2 backbone without PoE power draws, or when your devices are all externally powered. If your goal is to minimize heat in a small crawlspace or you simply want a clean management interface without PoE, the US 24 shines. On the other hand, if your deployment includes a handful of PoE devices, a PoE capable sibling will reduce the number of devices in your network rack and simplify cabling, at the cost of extra heat and power usage. In short, pick the non PoE for a clean, silent data backbone, and move to PoE variants when you need to power devices from the switch itself.

## Real world deployment scenarios

- Home lab with multiple VLANs for test labs, staging networks, and a separate management network
- Small office with guest networks and printer VLANs, where PoE devices are on dedicated PoE switches but the core backbone remains on non PoE switches for efficiency
- Hybrid environments where IP cameras or PoE devices are connected to a PoE edge switch while the core backbone remains fast and predictable on the US 24

## Buying options and references

For more official details and current pricing, visit the UniFi product page for the US 24 on the official store:
- External product page: https://store.ui.com/products/unifi-switch-us-24

If you want a broader context about UniFi deployments, you can read our related posts linked here for deeper dives into setup and design principles:
- Basic UniFi setup guide: {% post_url 2025-02-15-unifi-setup-guide %}
- Network design 101 for small offices: {% post_url 2024-11-08-network-design-101 %}

## Final take and recommendations

The UniFi US 24 is a reliable, quiet, and manageable option for a 24-port non PoE switch in small offices and home labs. If your goal is to build a sturdy network backbone with clear management, VLANs, and a clean dashboard, this switch delivers with the usual UniFi polish. Its lack of PoE makes it a simpler unit with fewer heat and power concerns, which translates into a calmer rack environment. If your deployment needs PoE power for cameras, phones, or APs, you should consider the PoE variants in the UniFi family. If you just want a sturdy 24-port backbone to tie devices together without PoE, this is one of the best options in its class.

In the end, you get a switch that blends into a modern network design without shouting for attention. It does its job and does it well, leaving you free to focus on upgrading the wireless access layer or expanding your VLAN strategy rather than wrestling with capricious hardware.

## Quick wrap up

- Great choice for a silent backbone in a home lab or small office
- Easy to manage with UniFi Network Controller
- Good uplink flexibility via SFP ports and LAG support
- No PoE, so plan PoE devices on separate gear
- Solid build, minimal noise, low heat

**If you are hunting for a dependable 24-port switch with a clean management experience and zero PoE drama, the US 24 is a compelling pick.**

**Buy via our affiliate link and support Geeknite while you level up your setup: https://affiliate.geeknite.com/unifi-us-24**
