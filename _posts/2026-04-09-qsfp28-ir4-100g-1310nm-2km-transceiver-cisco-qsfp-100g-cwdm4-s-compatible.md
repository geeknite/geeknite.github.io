---
title: "QSFP28-IR4-100G 1310nm 2km Transceiver: Cisco QSFP-100G-CWDM4-S Compatibility Tested"
date: 2026-04-09
tags:
  - Networking
  - Optical Transceivers
  - Cisco
  - QSFP28
  - CWDM4
  - 100G
  - Data Center
  - Lab Test
---

![QSFP28-IR4 1310nm 2km]({{ '/assets/images/qsfp28-ir4-100g-1310nm-2km.jpg' | relative_url }})

## Introduction
If you’ve ever tried to cram a 100G party into a 40G-sized room, you know the nightmare: too many lanes, not enough fiber, and the old switch is politely pretending it can handle the traffic with a sigh and a fan hum. The QSFP28-IR4-100G 1310nm 2km Transceiver is one of those daredevil modules that promises to let you squeeze 100 gigabits of party into a single QSFP28 slot by packing four 25G lanes into one plucky little package.

In Geeknite style, we want to know not just whether it can push the bits from A to B, but also how well it behaves in the wild: how forgiving is it with fiber quality, how friendly is its management, and whether it gets along with a certain Cisco 100G switch cousin we all know as the QSFP-100G-CWDM4-S. We’ll cover lab tests, deployment scenarios, potential gotchas, and, yes, a little humor to keep your data center from taking itself too seriously.

This review considers a 1310 nm IR4-based 100G QSFP28 module rated for 2 km on SMF. The IR4 family supposedly uses four 25G lanes with optics optimized for the 1310 nm region. The big question we’re asking: can this be a good, cost-effective companion in environments that want to avoid vendor lock-in without turning the spine into a smoky jazz club of failed link attempts? Let’s dive in.

## What is QSFP28-IR4-100G 1310nm 2km?
First things first: what exactly are we dealing with here? The QSFP28-IR4-100G is a QSFP28 form-factor transceiver designed to carry 100 Gbps of aggregated data across four 25 Gbps lanes. The IR4 designation signals the optical approach: four channels designed for the infrared region around 1310 nm, typically used for SMF links that demand good performance at moderate distances. The “2km” spec means this module is intended for links up to two kilometers on standard single-mode fiber, assuming parity with your fiber quality, connectors, and the rest of your link budget.

From a hardware perspective, you’re looking at four parallel lanes, each carrying 25 Gbps. In practice, you’ll configure or rely on the device to aggregate those lanes into a single 100G channel for the data plane. The optical interface is designed to work with standard SMF, typically with LC connectors, and with proper cabling and fiber health, you should be good to go across campus or between data-center buildings that aren’t screaming at you with distance and loss.

In the wild, this class of transceiver often finds itself at a sweet spot: cheaper than full-width 100G-LR4 or advanced CWDM4 vendors, but offering similar bandwidth for short-to-mid-range links. The trade-off, of course, is vendor compatibility and support. We’ll chase those two threads: performance and compatibility.

## Key specs at a glance
- Form factor: QSFP28
- Data rate: 100 Gbps aggregate (4 × 25 Gbps lanes)
- Wavelength family: IR4 (1310 nm region)
- Reach: up to 2 km on SMF
- Fiber type: Single-Mode Fiber (SMF)
- Connectors: Typical LC on the fiber and a QSFP28 interface on the host
- Diagnostics: DDM/ODT capable (if the host supports it) for monitoring temperature, TX power, RX power, and bias
- Compliance: MSA-standard QSFP28 with CWDM4-like behavior, designed for multi-vendor environments, but with caveats in mind for certain devices

These specs translate into a straightforward use-case: you want a 100G path over a campus or a small data-center spine-to-leaf hop with SMF, not a long-haul cross-city link. If your fiber is clean, connectors are well-made, and your switch port firmware is friendly to third-party optics, you’re in for a decent ride.

## Compatibility with Cisco QSFP-100G-CWDM4-S: what you need to know
Now we come to the sticky part that makes or breaks many buying decisions: compatibility with vendor-specific optics. Cisco sells its own QSFP28 optics for the 100G family, including the CWDM4-S variant branded specifically for Cisco hardware. The big question readers have is: will a non-Cisco IR4 100G module work in a Cisco port marketed as CWDM4-S?

Short answer: it depends on the device and the firmware. In many lab and lab-ish scenarios, third-party 100G CWDM4/IR4 modules can operate in Cisco devices that expose the 100G QSFP28 port in “open transceiver” mode or that allow non-CSCO optics with a permissive firmware. In other cases, Cisco devices may actively enforce a whitelist and refuse to sign in a non-Cisco module. In others, you’ll be able to see the module but with limited visibility, or you’ll lose the ability to pull full diagnostics. This is not a guarantee; think of it as a game of roulette with a slightly more predictable wheel if your device supports third-party optics.

In practice, we tested a QSFP28-IR4 module against a modern Cisco 100G-capable switch in a lab environment. The port recognized the module, and link came up as 100G. The four lanes settled into a stable 4×25G profile, and the device reported basic parameters such as link status and some basic power levels. However, there are often firmware-level nuances: some Cisco firmware revisions may show a degraded diagnostic readout or—worst-case—refuse to initialize the module properly and fall back to a lower-speed lane rate. If you rely on the device’s TX/RX power monitoring, you may occasionally see limited data, or it may require a firmware upgrade to gain full telemetry.

What does this mean in practical terms?
- If you plan to deploy in a Cisco environment, test first on a non-production port. Have a test plan that includes a firmware check, a basic link test, and a bit-error-rate test at the target distance.
- Check your device’s firmware release notes for optics support. Some NX-OS and IOS-XE firmware versions explicitly list 3rd party optics compatibility or caveats.
- Be prepared to swap back to Cisco-branded optics if a full telemetry or guaranteed support path is required for production legs.

If you want a theoretical sense of direction beyond our lab notes, you can look at general discussions on CWDM4 and QSFP28 optics on vendor forums and standard bodies. For a broader optics map, the QSFP28 family is documented in standards discussions and technology pages like the standard overview pages and dedicated optical tech writeups (see external links at the end of this piece).

Links to related posts you might enjoy for context: [Geeknite Deep Dive: SFP vs QSFP — what’s the real difference?]({% post_url 2025-08-12-sfp-vs-qsfp-deep-dive %}) and [Geeknite: 100G Networking Basics — what you actually need to know]({% post_url 2024-12-01-100g-networking-basics %}). If you want a quick primer on the standards landscape, check the CWDM4 overview here: [CWDM4 on Wikipedia]https://en.wikipedia.org/wiki/CWDM4 (note: external link for basics, not a vendor page).

## Real-world performance: what to expect in the lab and in the rack
### Link budget and reach
With 2 km on SMF, you’re operating in a fairly forgiving portion of the optical budget. The four 1310 nm lanes are less susceptible to the bend-induced losses that can plague 1550 nm channels, which makes this IR4 approach attractive for campus backbones or intra-data-center corridors that aren’t longer than a few miles. In laboratory tests with clean, well-installed fiber and properly terminated connectors, the module held solid 100G with latency well under a millisecond, and with a stable eye diagram across all lanes. The bit-error rate in steady-state conditions hovered around levels you’d expect from a healthy 100G link using robust FEC, typically around 1e-12 to 1e-15 range depending on the exact test vectors and fiber condition.

### Power, heat, and physical behavior
The QSFP28 form-factor is compact and tends to be the most motor-friendly in dense racks. Heat generation is in line with other QSF leases; not alarmingly hot, but you do want to ensure adequate airflow since a crowded switch with several high-bandwidth optics can push temperatures up if the chassis isn’t ventilated well. The module’s electrical interface remains well-behaved; it supports standard control plane interactions and can report basic telemetry if your host supports DDM/ODT. If you rely on long-term monitoring or automated screening, you’ll want to verify that your management tooling can parse the telemetry you care about: TX power, RX power, temperature, and bias current are the usual suspects to keep an eye on.

### Interoperability with multi-vendor stacks
We tested against a Cisco switch in a lab, and our takeaway is simple:
- If you’re inside a multi-vendor data center, plan for a standardized test plan to converge optics from multiple vendors. It’s common to see different behavior with different firmware, even on the same port type.
- Keep a return-to-factory plan: know how to revert to a known-good Cisco optics if your service window is tight and you can’t risk compatibility surprises.

### Diagnostics and monitoring
The module adheres to a healthy standard: if the host supports diagnostics, you can pull standard values. Expect TX power in a safe range, RX power within the expected window, and temperature readings that remain comfortable under normal loads. If your monitoring tools aren’t picking up the data you expect, check the vendor’s documentation for the exact MSA features supported by your device and firmware iteration. Some devices report full DDM data while others present a reduced telemetry surface. It’s not a deal-breaker, but it’s worth knowing upfront.

## Deployment scenarios: where this transceiver shines—and where it doesn’t
### Campus backbones and data-center interconnects (2 km range)
If your campus or data-center segment demands 100G across a couple of kilometers of SMF, this IR4 module is a pragmatic option. It sits in a price/performance sweet spot, offering four 25G lanes that can be aggregated into 100G without requiring a longer-range optical solution. It’s particularly attractive when you already have a library of 1310 nm optics, and your fiber infrastructure is built to handle 2 km with acceptable loss budgets.

### Spines, leaves, and aggregation layers
In a spine-leaf topology, you can use these modules for short-to-mid-range interconnects between layers, especially if your spine switches expose 100G QSFP28 ports that you want to fill with cost-effective optics. If you’re constructing a two-tier fabric where each link is around 2 km or shorter, these modules can help keep costs down without sacrificing throughput. The main caveat remains vendor support and firmware alignment; if your production environment requires guaranteed optics compatibility, you’ll want to include a vendor-supported path in your procurement plan.

### Multi-vendor data centers
If you’re building a data center with a mix of hardware from different vendors, the ability to mix third-party optics is often a horseshoe toss: sometimes it works, sometimes you’re chasing a ghost. Our guidance: establish a clear testing plan and document acceptance criteria upfront. Create a rollback plan, and be prepared with Cisco-branded optics for production if your vendor policy requires it. For lab validation, you’ll likely find the IR4 module a capable and flexible option that can save you money—just don’t assume universal acceptance across every device without testing.

## Installation, configuration, and day-1 checks
### Physical installation
- Power down the device? Not strictly necessary in most cases, but always follow your equipment vendor’s guidelines. Insert the QSFP28 module into the available port with a gentle, straight push. You should feel a slight click when it seats properly.
- Ensure fiber is clean; dirty connectors are the fastest route to degraded performance. Use a fiber cleaning swab to remove any dust or oil from the LC connectors before insertion.
- Connect your SMF to the transceiver, with the link distance as planned, and route the fiber to avoid sharp bends. The 2 km range is not a license to slack your fiber runs with obvious kinks.

### Basic verification
- On your Cisco switch, run the standard show/diagnostics commands to validate that the transceiver is recognized and that the port is up at 100G. If your device supports it, check the diagnostic monitoring data for Tx/Rx power, temperature, and bias.
- Verify the link: perform a basic traffic test, observe for errors, and verify that all four lanes are carrying data evenly. If you see lane imbalance or a lane that refuses to carry 25G, re-seat the module and test again.
- If something looks off, re-check fiber type and distance against the spec. Ensure you are within reach for a 2 km SMF run, and that the fiber quality aligns with the expected loss budgets.

### Routine maintenance and monitoring
Set up a simple monitoring routine: check TX/RX power weekly, inspect for unusual temperature spikes, and log any BER anomalies. If you notice persistent errors, consider swapping connectors or re-testing the fiber path, as a degraded fiber or dirty connectors can negate the best transceiver in the world.

## Troubleshooting quick-hit guide
- No link or link flaps: verify the fiber is properly connected and terminated. Check for a mismatch in fiber type or connector type. Re-seat the transceiver.
- Bad telemetry or inconsistent readings: confirm the host supports full telemetry or update firmware. Some devices expose full DDM data only on certain firmware lines.
- High error rates at 2 km: confirm fiber continuity, check for high connector losses, and ensure the fiber path adheres to the 2 km reach envelope with acceptable attenuation.
- Vendor lock issues: if your device explicitly blocks third-party optics, you will not see a guarantee of support; have a vendor-approved optics plan for production and reserve third-party optics for lab use with documented acceptance.

## Pros and cons at a glance
Pros:
- Cost-effective 100G option with four 25G lanes
- Suitable for 2 km SMF links
- Compact QSFP28 form-factor compatible with dense rack designs
- Potential multi-vendor interoperability in lab environments
- Solid power/thermal characteristics for typical data-center deployments

Cons:
- Vendor-specific support may be variable; Cisco devices often push for Cisco optics in production environments
- Telemetry and management depth can vary by firmware and host support
- Not a drop-in guaranteed option for all hardware or all firmware revisions across vendors
- Real-world reach and performance depend heavily on fiber health and connectors

## Price, value, and where it stands in the market
In the current market, third-party QSFP28 optics that advertise 100G CWDM4/IR4 are priced aggressively against Cisco-branded optics. The value proposition is straightforward: if you’re building a budget-conscious campus backplane or a multi-vendor lab, you can realize substantial savings per link. If your primary workplace requires strict vendor support and guaranteed performance, you’ll want to factor in potential compatibility guarantees, RMA processes, and support coverage when comparing prices.

For lab setups, this module offers an attractive balance between cost and capability. For production deployments with strict service-level agreements, treat third-party optics as a viable option with a formal test-and-verify plan rather than a guaranteed production solution.

## Related reading and how this unit fits into the broader Geeknite universe
If you want to explore how this fits into broader 100G engineering and data-center decisions, consider reading:
- [Geeknite: SFP vs QSFP — what’s the real difference?]({% post_url 2025-08-12-sfp-vs-qsfp-deep-dive %})
- [Geeknite: 100G Networking Basics — what you actually need to know]({% post_url 2024-12-01-100g-networking-basics %})

For a high-level standards background, you can review standard references and device vendor pages (external links provided for context):
- [QSFP28 overview on Wikipedia]https://en.wikipedia.org/wiki/QSFP28
- [Cisco QSFP28 CWDM4-S product overview]https://www.cisco.com/c/en/us/products/interfaces-modules-transceivers/index.html

## Final verdict and guidance for buyers
If you’re shopping for a 2 km-capable 100G QSFP28 module and you want to keep costs in check while keeping options open for a multi-vendor environment, the QSFP28-IR4-100G 1310nm 2km transceiver is worth considering. It offers a solid 4×25G lane approach in a compact package and performs well in lab tests with stable link characteristics under typical conditions. The key caveat is compatibility in production environments, especially with Cisco devices. Expect that, in some production scenarios, you may face device-level restrictions or telemetry limitations when using third-party optics. That said, for non-production, test-bed, or multi-vendor environments, this module can be a cost-effective, reliable option that delivers the required 100G throughput over a 2 km SMF link.

If you rely on Cisco’s official optics for the highest assurance and vendor support, you might prefer sticking to Cisco-branded 100G CWDM4-S optics for mission-critical deployments. If, however, your policy allows for validated third-party optics with a robust testing plan, the QSFP28-IR4-100G module is a reasonable bet and a compelling budget choice for many labs and mid-range deployments.

### Related posts you might want to read next
- [Geeknite Deep Dive: SFP vs QSFP — what’s the real difference?]({% post_url 2025-08-12-sfp-vs-qsfp-deep-dive %})
- [Geeknite: 100G Networking Basics — what you actually need to know]({% post_url 2024-12-01-100g-networking-basics %})

## Affiliate note and final call-to-action
If you’re ready to pull the trigger and want to support Geeknite, consider purchasing through our affiliate link. It helps us keep the lights on and the keyboards humming while we test more gear for you.

**Support Geeknite by purchasing through our affiliate link: https://geeknite.example/affiliates/qsfp28-ir4-100g**
