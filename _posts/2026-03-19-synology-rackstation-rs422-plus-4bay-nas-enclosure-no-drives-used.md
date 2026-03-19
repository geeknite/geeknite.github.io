---
title: 'Synology RackStation RS422+ 4-Bay NAS Enclosure, No Drives, Used'
date: 2026-03-19 12:00:00 -0000
tags:
  - NAS
  - Synology
  - RackStation
  - UsedEquipment
  - TechReview
---

![RS422+ in a rack](./assets/images/rs422plus.jpg)

Welcome, fellow digital packrats. If you’ve ever wandered into a mid-sized data center or a tech thrift shop and seen a rack-mounted box with more HDD bays than hot takes on social media, congratulations: you’ve met the Synology RackStation RS422+ 4-Bay NAS Enclosure. And yes, it is exactly as dramatic as the name sounds. This particular unit comes with no drives included and, presumably, a history of being both powerful and politely annoyed by the word “NAS” shouted at it across a LAN. Our mission today: determine whether this used chassis is worth your money, your time, and the inevitable battle with dusty drive sleds.

In Geeknite terms: the RS422+ is a chassis that wants to be your data’s best friend, provided you feed it the right drives, a DSM-compatible brain, and a sense of humor about spare parts and cable spaghetti. It’s a 4-bay rack-mount enclosure, meaning it wants to live in a proper server rack and help you hoard terabytes with a quiet, businesslike buzz. It does not come with drives, so if you were hoping for a plug-and-play “drop-in four 4TB drives and go” experience, you’re going to have to supply the disks yourself—and maybe a new case of coffee, because assembling a NAS is basically hardware LEGO with less certainty about whether you’ll end up with a dragon built from airflow.

If you want to nerd out about official specs before you commit real gear to a real rack, you can peek at the official product page: [Synology RS422+ product page](https://www.synology.com/en-us/products/RS422+). And if you’ve already sworn eternal loyalty to other device ecosystems, there are plenty of more generic guides—like our NAS basics posts—to help you translate this chassis into a working home or small-office server. See {% post_url 2024-04-15-nas-basics.html %} for the high-level run-down, or {% post_url 2025-11-20-raid-extensions.html %} if you’re curious about how you might expand your array later on.

Unboxing a used RS422+ is a different kind of surprise than unboxing a new gadget. You’ll get a sturdy metal frame, drive bays with hot-swap trays, a front-panel activity light aesthetic that looks like it means business, and a rear I/O panel that reads like a middle school sci-fi novel. The build quality is the kind of sturdy you only notice when you carry it: heavy enough to remind you that no, this is not a toy, but not so heavy you have to recruit a small moving company to get it into your rack. The plastic sliders and metal brackets have that “tough but not brittle” feel, which for a used piece is exactly what you want. If you’re hoping for the pristine shininess of a brand-new unit, you’ll be disappointed. If you’re hoping for a reliable chassis that can keep a bunch of drives alive and humming in a home-lab or small office, you’ll likely be pleasantly surprised.

Before you pull the trigger, let’s layout what you’re getting—and what you’re not getting—with this enclosure. The RS422+ is designed to hold 4x SATA drives and to be installed in a standard 19-inch rack. That means front-access bays, hot-swap drive sleds, a manageable front-panel UI, and—crucially for used purchases—a potential for misaligned trays or slightly wobbly rails if the unit has spent a few years in shipping boxes, under-a-dan-construction zones, or the back of a warehouse floor. It does not include drives, RAM expansions, or DSM software. You’ll supply the brains (DSM-compatible OS) and the brawn (the disks, and perhaps a PCIe card if you want to upgrade network throughput).

Design and Build: The chassis feels like a purposeful piece of hardware rather than a consumer gadget. The RS422+ uses a 2U form factor with four drive bays aligned in a row. The front panel is your usual mix of drive sleds, status LEDs, and minimal branding—enough to tell you what’s wrong without a PhD in signal processing. The hinges and trays are the kind that survive a light touch of a forklift or two, which is a weird form of reassurance when you’re shopping used. Build quality is the kind that makes you feel comfortable doing a small home-lab raid of data replication rather than risking a shake-and-bake with an unboxed brick in your living room. The power supply sits at the back; the fans float around the interior like tiny helicopter pilots watching drive activity from behind the curtain. If you’re picky about acoustics, the RS422+ isn’t a whisper, but it isn’t a jet engine either—think “office-quiet with the occasional whoosh of cooling fans” rather than “hurricane in a data center.”

The I/O panel, as you’d expect, includes enough connections to make every network administrator smile and then cry a little inside when they realize they’ll be negotiating switches and cables to make it work. Expect standard gigabit or 2.5GbE/10GbE expansion options depending on your exact model and the PCIe cards you pair with it. If you’re planning to use this in a mixed environment (Windows, macOS, Linux), you’ll be leaning on SMB/AFP/NFS protocols, with DSM handling authentication and user management. The important part is: this is a thing you put in a rack, connect to a switch, and then pretend you’re a data wizard when your LEDs do the right dance.

Disk compatibility is where the rubber meets the road. You’ll want 3.5" SATA drives for the primary bays, with 2.5" bays often possible via adapters—though you’ll want to confirm that your unit supports 2.5" drives in all bays if you go that route. A good rule of thumb is: use drives designed for NAS use, with vibration tolerance and reliability under continuous operation. You’re not buying a gaming rig; you’re building a 24/7 storage appliance, so endurance matters.

Performance and Throughput: In a NAS of this class, the headline numbers usually come from CPU, RAM, and network connectivity. The RS422+ typically ships with a modest but capable CPU for a 4-disk enclosure, plus a few gigabytes of RAM that you’ll likely want to bump up if you’re doing heavy media streaming, encryption, or multiple users hammering the disks at once. Real-world performance is often governed more by your drives and network than by the chassis; a fast SATA SSD cache could help with hot data, but the boring truth is that your NAS’s speed is the speed of your disks plus the speed of your network. If you’re streaming 4K video, you’ll want a robust network path and enough RAM to handle metadata and file indexing. If your use case is archive storage with occasional retrieval, you’ll be happier with capacity over raw throughput.

One thing that catches people by surprise with used units is software state. If the previous owner didn’t perform regular DSM updates, you may be dealing with an older OS version and possibly unsupported features. In practice, you’ll want to do a factory reset in DSM, update to the latest supported version for your hardware, and then configure user permissions and shares from scratch. This is not a plug-and-play consumer gadget; it’s a tiny server unfurling its cognitive gears in your living room or office.

A note on noise and power: the RS422+ uses fans that wake up with drive activity. In a well-ventilated rack, they’re not loud enough to disrupt a podcast, but in a small quiet room they’ll be audible when the drives spin up. Power draw is in the NAS-typical neighborhood—more than a Raspberry Pi, less than a full-on NAS cluster. If you’re upgrading an older home lab, you’ll appreciate having a dedicated rack space where you don’t have to coax the unit to stay out of the living space.

Setup and Configuration: Here’s where the reality check lands. A used RS422+ requires you to supply disks and to load the DSM operating system. Step one is physical installation: mount the chassis in your rack, connect the power, and slide the drives into the four bays. Step two is network setup: connect the NAS to your switch, boot, and verify that the DSM installer can reach the device. Step three is infamous: configure storage pools, RAID levels (e.g., RAID 5 or RAID 6 for 4 bays, or a more exotic RAID 10 if you’re feeling lucky), and set up shared folders and users. If you’re new to NAS design, this is where you’ll spend a lot of your time learning about data redundancy, parity, and the differences between single-disk versus multi-disk resiliency.

The DSM interface is user-friendly by NAS standards. It’s not iOS-simple, but it’s not a black hole either. Expect wizards to guide you through volume creation, share permissions, and basic services like File Station, Photo Station, and Backup. If you’re migrating from another vendor’s OS, DSM’s package center is where you’ll install extra apps for backups, media servers, or cloud sync. You’ll likely want to enable automatic firmware updates and enable two-factor authentication for security, especially if the NAS is accessible from the internet via port forwarding or a VPN.

Used Purchase Considerations: If you’re buying a used RS422+, you’re evaluating risk, value, and future-proofing. Here are practical checks:
- Inspect the chassis for dents, bent rails, or loose parts. If the front panel feels rattly, that’s a red flag. If the drive sleds slide smoothly, you’re in good shape.
- Check the power supply and fans. A failing PSU can be expensive to replace, and noisy fans can ruin a quiet room experience. If you can, run the unit for a while during a live test bench and listen for abnormal noises.
- Verify that the rails and mounting hardware are complete. A rackmount enclosure without rails is a mechanical question mark.
- Confirm no drives are included, obviously, but also verify that your chosen drive bays aren’t blocked by misaligned trays or dust buildup. A clean interior is a good omen.
- Consider the warranty status. Used gear may have limited or no warranty. Decide whether you’re comfortable relying on a DIY DSM setup and your own backup strategy.

Drive configurations: You’ll want a plan for disks before you even power up. With 4 bays, you can implement RAID 5 or RAID 6 for redundancy, or you can go with RAID 0 for performance (not recommended for data resilience). If you want to maximize capacity with a touch more resilience, RAID 5 is a good default for four bays; RAID 6 adds extra redundancy but reduces usable capacity a bit more. If you’re paranoid or data-heavy, RAID 10 can provide excellent performance and redundancy, but you’ll lose some usable space. In practice, the best choice depends on your tolerance for drive rebuild times and your backup strategy outside the NAS itself. Always keep a separate backup of critical data, because even the best RAID array isn’t a guarantee against user error or drive failure.

Where this unit shines: a used RS422+ is appealing for someone who wants a compact, rack-mable, four-disk storage solution without paying for a brand-new appliance. It’s ideal for a small homelab, a thoughtful home media server with streaming capabilities, or a small office file server where the data footprint isn’t million-user scale but still meaningful. If you’re considering running media servers (Plex, Jellyfin), backups, or centralized file sharing for a handful of machines, this chassis gives you a robust platform with room to grow.

Where this unit might not be ideal: if you’re chasing cutting-edge performance, 10GbE, or hot-swapping dozens of drives in a single enclosure, you’ll likely outgrow the RS422+ quickly. For these use cases, you’d be better served by newer, more scalable NAS appliances or a dedicated server with a larger PCIe expansion strategy. It’s also worth noting that, with used gear, software support can become a moving target. DSM updates can be prudent, but sometimes a stubborn older OS version lags behind security advisories or new features. If you require the latest feature set, a new unit with current software support may be a better long-term investment.

A few additional notes on ecosystem and compatibility: this enclosure is intended to work with Synology’s DiskStation Manager (DSM). You’ll want to ensure your drives are DSM-compatible and that you’re comfortable with a Linux-based OS underneath the hood. If you’re migrating from a different brand, you’ll appreciate how DSM treats storage differently from Windows-based shares, with user permissions and share-level controls giving you a lot of control over who can access what. And yes, you’ll be tempted to turn on encryption for sensitive folders; just remember that encryption adds overhead (and CPU usage) during data access, so plan accordingly if you’re dealing with large media libraries or high-throughput workloads.

External references (for more reading):
- Product page: https://www.synology.com/en-us/products/RS422+
- NAS basics primer: {% post_url 2024-04-15-nas-basics.html %}
- RAID strategies explained: {% post_url 2025-11-20-raid-extensions.html %}

Final thoughts on the used RS422+: this chassis is a sensible, cost-conscious way to get four drives into a rack with a DSM-backed layer of software. It won’t be a top-of-the-line performance monster, but it won’t be a furniture-grade paperweight either. The decisive factor is your drive choice, age of the unit, and whether you’re comfortable building a small data server ecosystem around it. If you’re patient, methodical, and want a nice blend of rack presence and storage capability, the RS422+ can be a worthy addition to your tech arsenal.

Pros:
- Solid physical build for a used chassis
- Four bays provide ample expansion without complexity
- Rack-mountable for clean data-center vibes in a home lab
- DSM-backed software ecosystem with a broad app catalog
- Flexible drive configurations and potential for expansion with PCIe

Cons:
- No drives included; you must source disks separately
- Used units may have variable warranty and firmware history
- Depending on the drives and network setup, you may need some time to tune performance
- Noise/power trade-offs in a quiet room versus a racks-in-a-dedicated closet

If you’re curious about a more budget-friendly way to start a NAS, you might also consider a DIY approach with a consumer motherboard in a small case; but if you want a polished OS-on-a-chassis experience with a professional-feeling UI and integrated data-management tools, the RS422+ is a compelling option in the used market.

How to decide: If your plan is to run backups for a handful of devices, centralize media storage, and maybe serve the odd virtual environment through containers on DSM, the RS422+ can be a sweet spot between price and capability. If you’re a performance hound who wants every bit of speed in real time and the ability to run dozens of VMs locally, you might want to look at more modern, higher-end options or a robust server build with more PCIe lanes and memory headroom.

Bottom line: used RS422+ 4-Bay NAS enclosures deliver a sturdy, rack-ready storage solution for homelabs or small offices. They strike a balance between capacity, manageability, and cost, as long as you go in with a plan for drives, backups, and DSM setup. They are not magic, but they’re dependable enough to be your data’s loyal sidekick if you treat them right.

Recommendation: If you’re in the market for a four-bay NAS chassis that you can drop into a rack, pair with a sensible set of NAS-grade drives, and run DSM with a robust backup plan, the RS422+ used unit deserves serious consideration. It’s a pragmatic, capable box that offers real value in the right hands. Just do the math on drive cost, warranty, and ongoing power usage before committing to the used-market gamble, and you’ll come out ahead.

Final words: in the grand scale of geeky storage, this is the kind of device that quietly powers your every day — a dependable chassis that carries the load without breaking the bank. It’s not a showpiece; it’s a workhorse. And sometimes, the quiet, dependable workhorse is exactly what you need to keep your data safe while you chase the next big upgrade.

If you’re ready to take the plunge, click this affiliate link and join the ranks of people who made friends with their data instead of wrestling with it:

**Support Geeknite by buying through our affiliate link: https://affiliates.geeknite.example/rs422?ref=abcd**