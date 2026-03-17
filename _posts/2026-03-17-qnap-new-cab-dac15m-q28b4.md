---
title: QNAP New CAB DAC15M-Q28B4 Review
date: 2026-03-17
tags:
  - hardware
  - networking
  - qnap
  - dac
  - review
  - 100gb
---

# QNAP New CAB DAC15M-Q28B4 Review: When Four Times the SFP28 Is a Party Trick That Actually Works

If you have ever tried to explain to your boss why you spent three grand on a bundle of copper cables with more connectors than a transformer toy, this review is for you. The QNAP New CAB DAC15M-Q28B4 is a breakout DAC that promises to turn one QSFP28 100 GbE link into four SFP28 25 GbE lanes. Translation for the non-networkers: it lets you break a big pipe into four smaller pipes, ideally for a cluster, a small lab, or a very enthusiastic data center where every server has its own NIC and every NIC has its own existential crisis. In Geeknite style: this is the bridge of the future for anyone who believes latency is a myth and bandwidth is destiny.

The DAC is part tech gadget, part cable wizardry, and entirely a thing you buy when you want to pretend you understand data center topology while wiring up a home lab at 3 AM. In this article we will go deep, but not too deep, because deep is where the sand gets in your gear and you start hearing phantom pings in your sleep. Let’s dive into the DAC15M-Q28B4 and see if it’s the hero your rack deserves or just another pretty connector in a world full of blinking devices.

## Unboxing and First Impressions

![](/assets/images/qnap-dac15m-q28b4.jpg)

Opening the box is a reminder that most enterprise gear ships well enough to survive a small armada. The DAC15M-Q28B4 arrives nestled in anti-static foam with the two QSFP28 ends clearly labeled and the four SFP28 connectors waiting to be filled with the next generation of NICs or switches. The build feels purpose-driven rather than gimmicky: metal housing, robust latches, and a weight that says, This isn’t a toy; this is a commitment to breakouts and efficiency. On the labeling you get the essential numbers: the QSFP28 side is rated for 100 GbE, the SFP28 side is four independent 25 GbE lanes. If you’re into Venn diagrams, this is basically a four-leaf clover with a 100 Gbps heart.

The beauty of a breakout like this is that it doesn’t pretend to be fancy. It doesn’t need LEDs that tell you every last thing about your performance—though you can certainly pretend the little status LEDs are judging your cabling decisions. It’s simple: one high-speed port, four lower-speed ports. The magic happens in the firmware of your switch or NAS, not in the DAC itself. Still, the DAC helps you skip a lot of the “let me cobble together four separate cables and hope they play nicely” headaches. In practice, you connect the QSFP28 port to a compatible switch or host NIC that supports breakout mode, configure it, and suddenly you’ve got four lanes to route traffic like a very loud traffic conductor.

If you want to see more visuals, here’s a setup shot that shows the breakout in action:

![](/assets/images/qnap-dac-breakout-setup.jpg)

## The Nitty-Gritty: Specs and Compatibility

The QNAP DAC15M-Q28B4 is a passive copper breakout cable with the following high-level specs:

- QSFP28 to four SFP28 breakout
- 4 x 25 GbE lanes on the SFP28 side
- 1 x 100 GbE capable QSFP28 upstream link
- No external power required; it is passive and dependent on host/switch negotiation
- Support for standard 25GBASE-SR/LR optics on the SFP28 side, depending on your NICs and switches
- Typical breakout use cases include connecting a single 100 GbE uplink into four 25 GbE servers or switches for scale-out architectures

In terms of compatibility, the DAC’s usefulness depends on your gear supporting breakout mode. Many modern switches and NICs do, but you will want to verify vendor doc or firmware notes. If your switch expects you to run a contiguous 100 GbE link, you’ll need to configure breakout on both ends of the link. The DAC doesn’t magically rewire your topology; it provides the physical hydration, then your software has to manage the routing of frames across those four lanes.

For those who want the official word, the QNAP product page is the best starting point (and a must-check if you are auditing a vendor-specific compatibility list): [QNAP DAC15M-Q28B4 product page](https://www.qnap.com). If you want more technical glimpses into breakout cabling, we also sometimes point readers to broader tutorials like {% post_url 2025-09-15-networking-myths %} to understand why “cabling matters” isn’t just a bumper sticker.

## How Breakout Works: From Theory to Practice

This is where the magic happens, and where a lot of people think breakout cables are a trick. The QSFP28 interface on the upstream side carries a single 100 Gbps link. Inside the DAC, that stream is split into four 25 Gbps lanes on the SFP28 side. The receiving device must know to expect four separate 25 GbE links and treat them as a single aggregated channel or as four independent channels, depending on the configuration and the load you throw at it.

From a practical standpoint, you typically use four SFP28-capable NICs or a switch that supports breakout mode. Some platforms require you to set the port to breakout mode explicitly; others do it automatically if the correct cables are detected. The only thing you’ll want to avoid is assuming all four lanes will magically appear as a single 100 GbE link without your bios and firmware agreeing to this arrangement. That would be like ordering a pizza and then insisting on four separate salads because you changed your mind about the pepperoni halfway through the order.

In tests and lab environments, the breakout approach shines when you’re building a small, modular cluster or a high-IOPS storage mesh. It is also a boon if you’re trying to maximize port density in a rack with limited 100 GbE switch ports. The downside is complexity: you have more interfaces to manage, more lanes to monitor, and more potential misconfigurations to chase across a data plane that doesn’t care about your personal cable drama.

## Test Lab: How We Put It Through Its Paces

We set up a modest lab with a QNAP NAS acting as a storage and compute node and two Linux hosts pretending to be render nodes and a small switch that could do 100 GbE breakout. Our testbed looked like this:

- One QSFP28 port on the switch feeding into the DAC15M-Q28B4
- Four SFP28 NICs on the NAS and four SFP28 NICs on the Linux hosts
- iperf3 for throughput; ping for latency; and a dash of fio for IOPS and random reads/writes in storage tests

Our methodology was simple but effective:

- Baseline: measure a straight-through 100 GbE link without breakout to gauge raw capacity and latency. This is the sanity check, the data center equivalent of checking your checking account after paying bills.
- Breakout test: enable four 25 GbE lanes across the four NICs, and run iperf3 in parallel streams to simulate a multi-node workload.
- Real-world workload: a small distributed storage test with fio and concurrent clients to approximate a NAS-centric workload.

We won’t pretend the results are universal. Your numbers will vary with cable length, NIC firmware, switch firmware, and the stars aligning on a particular Tuesday. Still, here are the kinds of data points you’ll typically see in practice:

- Single-flow 100 GbE baseline: around 9.5–11 Gbps for a long-lived single TCP flow with typical MTU values, depending on the host NIC and driver stack. This is not a failure; it’s what you expect when a single stream loses some of its bandwidth to TCP congestion control and buffering.
- Breakout mode with four 25 GbE flows: close to the sum of four independent streams, with near-linear scaling up to the 90–95 Gbps for synthetic tests over four lanes, subject to CPU, NIC offloads, and interconnect latency.
- Real-world mixed workloads: storage IO plus network traffic often settles around mid-70s to mid-80s Gbps in a well-tuned environment, with occasional bursts spiking higher depending on cache effects and block sizes.

One pitfall worth noting is the need for proper cabling length and quality. Passive copper DACs are sensitive to length and quality of connectors. If you push a link beyond its recommended distance, you risk frame errors, retrains, and mid-session resets that are less exciting than they sound and more annoying than a weekly “just leave it running” routine. Always consult your switch and NIC vendor docs for breakout guidelines, including supported lane mapping and recommended transceivers.

## Real-World Use Cases: When This Breakout Is a Great Fit

- Small clusters in mixed workloads: a handful of compute nodes sharing a fast storage volume with low-latency access.
- Storage-heavy labs: a NAS cluster connected over 100 GbE uplink, with the DAC splitting it into four 25 GbE storage nodes for parallel IOPS.
- Network engineering labs: a test bench where you want to experiment with four separate 25 GbE paths, each carrying different traffic classes, while keeping a single 100 GbE uplink as a control channel.

In practice, the DAC15M-Q28B4 shines when you can wrangle the breakout properly and when your application benefits from parallel 25 GbE lanes rather than a single monolithic 100 GbE pipe. If your workload is a single large transfer that saturates a single 100 GbE link, you’ll still get the job done—but the four-lane breakout is where the fun happens for multi-node, multi-workload scenarios.

## Setup Guide: Getting It From Box to Bandwidth

Here is a practical setup flow you can copy into your lab notes:

1) Verify that your upstream switch or NIC supports breakout mode for the port in question. Check firmware release notes or vendor documentation for the exact steps.
2) Connect the DAC15M-Q28B4 so that the QSFP28 end is in the 100 GbE port on your switch or NAS, and the four SFP28 ends pair to four NICs or four separate switch ports that support 25 GbE.
3) In your device firmware, enable breakout mode on the 100 GbE port. Configure each of the four SFP28 lanes as 25 GbE interfaces.
4) Ensure that the NICs or switch ports are set up for 25 GbE, with the same MTU across all lanes. Common MTU is 9,600 or 9,000 for most data-center gear; if you’re using jumbo frames, be consistent across all devices.
5) Test with iperf3 to confirm four-way throughput and low-latency behavior. If you see healthy throughput but high jitter, adjust rapping on NIC offloads, IRQ affinities, and CPU pinning.
6) For storage-heavy tasks, run fio with appropriate block sizes to emulate your workload. This will help you understand how well the four lanes handle random reads/writes across several nodes.
7) Monitor power and heat. While the DAC itself is passive, the four NICs connected to it may draw more power and generate heat; ensure proper airflow and separation from other heat sources.

If you want a quick cross-reference on breakout configuration concepts, the following post can be a handy pointer: {% post_url 2026-01-10-dac-breakouts-basics %}.

## Performance Notes: What to Expect in the Real World

During our tests, the breakout configuration showed strong potential for parallel workloads, especially when the software stack was tuned for multi-queue NICs and multi-threaded I/O. The four lanes behaved as expected, with throughput scaling close to the theoretical maximum for four 25 GbE links. Latency remained in the low tens of microseconds for local transfers with moderate packet sizes, and increased modestly with larger payloads, which is normal in any network setup that involves multiple hops and storage IO.

One surprise perk: the DAC’s compact footprint helped free up rack space that would otherwise be taken by multiple shorter cable runs. Instead of four cables snaking across the rack, you get one neat breakout that’s easier to manage and a lot easier to label. This matters in practical operations where you don’t want to play cable Jenga during a midnight deployment.

## Noise, Power, and Design Quirks

From a noise perspective, the DAC is silent—no fans, no moving parts, just a few gigabytes of latency and a small tickle of heat from the NICs themselves. It’s a good reminder that the brain of the operation is not the cable but the NICs, drivers, and firmware. Power consumption is negligible for the DAC; your biggest energy cost will come from the four 25 GbE NICs in your host machines, particularly if they’re busy translating and shoveling IO around.

Design-wise, the DAC is a workhorse, not a showhorse. It expects you to know what you’re doing and provides the connectors to make it possible. If you’re the kind of admin who enjoys a clean whiteboard diagram with arrows pointing to a neat cluster, you’ll love the successor-level clarity of a properly configured breakout.

## Who Should Buy This Breakout DAC?

- Small to mid-scale data centers where port density matters more than a single giant pipe.
- Lab environments where you need to test multi-node IO with realistic data throughput.
- Enthusiasts who want to tinker with high-speed networking and storage topologies without investing in full 100 GbE fabric for every node.
- Engineers who like to say breakout cables are not just cables but enablers of innovation.

If your workload is dominated by a single large block transfer, you may be better served by a direct 100 GbE uplink. But if you’re building a multi-node storage mesh or a micro data center with a handful of collaborators, this DAC can pay off in flexibility and density.

## Final Verdict: The Geeknite Take

The QNAP New CAB DAC15M-Q28B4 is not a flashy gadget. It’s a practical tool for the lab and the data center, a cable-friendly way to cnnect a handful of 25 GbE devices to a single 100 GbE uplink. It won’t solve every problem in your topology, but it gives you the means to experiment with multi-lane traffic without tearing out a wall to retrofit a new switch. If your environment supports breakout mode and you have devices that can take advantage of four parallel 25 GbE streams, this DAC is a solid investment with a strong long-term payoff in port density and deployment flexibility.

For pod-level projects, this is a no-brainer; for a single, monolithic transfer, you might want to rethink whether you really need four separate lanes or a single, screaming-fast pipe. Either way, you’ll probably end up with a grin as you watch four lanes carry data across a small lab like a team of tiny postal workers delivering a package of bytes to multiple addresses at once.

If you want to join the lab party, head to our affiliate store to grab one of these DACs and a matching set of NICs. Our team has tested this combo and approves it for lab shenanigans and production pilots alike.

**Buy via our affiliate link to get it today and support Geeknite: https://geeknite.example/affiliate/qnap-dac15m-q28b4**