---
title: 'Synology RackStation RS422+ 4-Bay NAS Enclosure, No Drives, Used: A Geeknite Review'
date: 2026-04-09
tags:
  - NAS
  - Synology
  - RackStation
  - Used
  - Review
  - HomeLab
  - Networking
---

## Introduction
If you ever wanted a compact data fortress that screams “we mean business but also we can nap elegantly on a rack,” the Synology RackStation RS422+ 4-Bay NAS Enclosure is likely to tug at your inner sysadmin with the enthusiasm of a caffeinated server rack. This is a used unit without drives, meaning it ships empty, hungry, and ready to be loaded with the kind of spinning doom your 2026 backups deserve. In Geeknite fashion, we’re going to take a spin through design, capability, caveats, and the inevitable reality that a used NAS is a friendship that often comes with a few invoices.

Below, we’ll cover what the RS422+ offers in a home-lab or small office context, how to pick drives for it (spoiler: no free samples here), how it performs when it’s actually working, and whether you should drop coin on this particular chassis or keep looking. Spoiler: if you want an all-in-one, rack-mm’d data snack bar with fancy pretend RAID names, this is a good starting point—but manage expectations like a calm adult with a cup of coffee and a plan.

> Pro tip: Always check drive health, fans, and the warranty status before you buy used. Synology warranty is usually per-device, not per-RackStation, and used gear is often more drama than a soap opera with a fast-forward button. Ok, enough pep talks—let’s dive in.

![RS422+ Front Panel](assets/images/rs422-front.jpg)

## Design and Build Quality
### The Chassis and Layout
The RS422+ is a 2U rackmount unit, designed to cradle four 3.5" or 2.5" drives in hot-swappable trays. The metalwork is the kind of sturdy you want when your data is the second-most valuable thing on the planet (right after your memes library). The front bears the familiar drive bays, LED indicators, and a simple control panel, all arranged in a way that feels intuitive even during a late-night, sleep-deprived firmware flush.

The enclosure’s build quality is a reminder of why Synology is popular: it’s not a flimsy box that flexes under the weight of a loose screw. The RS422+ knew it was a rack unit and behaved like a grown-up, which is weirdly comforting in a market full of RGB-lit toys.

### The Back, Ports, and Expansion
On the rear, you’ll find the interfaces that actually make the magic possible: network ports, PCIe expansion (for NICs or accelerator cards), and a power supply that better hope your electricity bill doesn’t decide to cosplay as a flamenco dancer.

In most configurations, you’ll get a couple of Ethernet ports (often 2.5GbE in the “+” models), with optional PCIe expansion to upgrade networking capabilities—because nothing says “future-proof” like a PCIe slot on a NAS that’s already five years old in spirit and design. There’s also cooling—fans that do their student-of-the-Internet thing and pretend they’re silent while they relentlessly push air over the drives and motherboard. If you’re assembling this in a small apartment closet, be prepared for a pleasant, slightly loud whirring soundtrack that says, “I’m serious about your data, but I also like air.”

### Images and Aesthetics
To get a sense of the RS422+ in the wild: front, back, and interior shots tell a story of practicality. The front is a mission control panel for drive bays, while the interior (when you crack the lid) reveals the motherboard, RAM slots, and the constraints of a tightly packed 2U chassis.

![](/assets/images/rs422-rear.jpg) 

## What’s Inside the RS422+ (and What You Should Expect)
### Drive Bays and Compatibility
This enclosure physically supports four drives. It’s a clean, sturdy platform, and because it ships without drives, you’ll be picking your own level of mechanical or SSD storage. If you’re a “layered redundancy” person, you’ll likely lean into a RAID configuration that balances performance and safety (SHR is Synology’s friend, and you should probably get to know it). Drives, you’ll want reliable SATA drives rated for NAS use: enterprise-ish grade if you’re affording it, consumer-grade with happy backups if you’re not.

### CPU, RAM, and Performance (Contextual)
Exact CPU and RAM specs can vary by Sigma‑level revision and region, especially with used units. In many RS422+ configurations, you’re looking at a capable x86-based processor and a reasonable amount of RAM for a 4-bay chassis. The implication is clear: this is not a toy for streaming ultra-high bitrate 4K on multiple streams from a single box without some tuning, but it is a robust foundation for backups, file sharing, and light media serving in a home lab or small office.

What this means in practice: expect the RS422+ to feel snappy for everyday tasks—file serving, user management, scheduled backups, and the occasional Plex/DLNA session—but don’t expect it to eclipse a modern multi-core NAS with a couple more NICs for your 8-in-1 home media ecosystem. It’s a mature platform that trades raw numbers for reliability and ecosystem polish.

### Networking: Interfaces, Peripherals, and CPU Affinity
One of the most appreciated aspects of futuristic NAS setups is the networking stack. The RS422+ often ships with dual network ports that can be bonded for throughput or used to segregate traffic (e.g., front-end clients vs. backup traffic). The option to add more NIC horsepower via PCIe is a win if your use case grows—think multiple clients, VLAN tagging, or a small business scenario where you want to isolate backups from general file sharing.

### Internal Design and Noise Considerations
In used gear, fans can be louder than a grown man in a gym, or surprisingly quiet if they’ve been replaced with reasonably efficient fans. The noise footprint is a thing to consider if you’re placing the unit in a home office closet or a basement room that shares air with your living space. There’s always a balance between long-term reliability (better fans, better airflow) and acoustic tolerance. If you’ve got a “studio space,” you’ll probably be fine; if you’ve got a home office next to your kitchen, plan for a little white-noise lacquer or a placement strategy that minimizes night-imposed WD-40-like coughs from the fan cage.

## Setup, First Boot, and Everyday Use
### Getting It Up and Running
The first boot on a RS422+ is a ritual—install RAM (if not pre-populated), slide in your drives, connect network cables, power up, and boot into the Synology DiskStation Manager (DSM) web interface. DSM is the star, with its familiar App Center, intuitive storage manager, and a few hyper-specific wizards that walk you through RAID setup, volume creation, and user permissions. If you’ve ever configured a NAS, you’ll feel right at home; if you’re new, you’ll feel like you’ve just been handed a spaceship with a friendly alien AI.

During the initial setup, you’ll be prompted to install DSM and configure your storage pool(s). The recommended approach is to set up a basic single-disk or RAID 1/5/SHR configuration depending on your need for data safety vs. usable space. If you’re giving this to a small office with a handful of users, an SHR setup (Synology Hybrid RAID) is a forgiving, future-proof choice that expands well as drives fail or are replaced.

### Data Safety and Disaster Recovery
Think about backups, not just on the NAS but from it. DSM has integrated backup solutions to replicate data to other Synology devices or to the cloud. You’ll want to configure snapshots for protection against accidental deletion or ransomware events. The RS422+ is a vehicle for both local redundancy and remote or cloud-based backups, so you can survive a local disk mishap and still wake up to your day with minimal panic.

### Performance Nuggets (That You Can Expect)
- Sequential file transfers with a 4-bay setup can saturate the network link provided by the built-in NICs when you’ve got 2.5GbE (or better via PCIe NIC) in play.
- Random I/O performance depends on the drives you pick and how you configure the RAID array; SSDs will dramatically improve metadata performance on a busy NAS, but HDDs can still excel for bulk file storage.
- DSM’s in-app apps for file syncing, media serving, and virtualization (depending on your license level) can be a multiplier for a small team or a power user.

## Use Cases: When RS422+ Shines (and When It Doesn’t)
### Home Lab and Enthusiasts
- Central file storage for creative projects and backups.
- A compact, rack-mountable media library server for households that want streaming and access from multiple devices.
- A learning platform for exploring RAID, DSM apps, and Docker (where applicable) without the “scary enterprise” label.

### Small Office/Workgroup Scenarios
- Shared file server with user permissions and versioned backups.
- Offsite backups or shared datasets for collaboration, with DMZ-like network separation via VLANs (if you’re comfortable with networking concepts).
- A testbed for new Synology DSM features before rolling them into your main production device.

### When Not to Choose RS422+
- If you need the absolute fastest SMB/NFS throughput you can get from a single box with 10GbE or more, you’ll probably want a platform with more aggressive NIC support and higher-end CPUs.
- If you’re expecting enterprise-grade support and warranty on used hardware, you’re best served with freshly manufactured gear from a vendor that offers a robust reseller warranty.
- If you’re not comfortable managing RAID/bandwidth tuning and DSM’s user permissions granularity, you might get overwhelmed and end up telling friends you’re just “buying a fancy network drive.”

## Buy Used RS422+? Here’s What to Check Before You Commit
- Drive health: If you plan to reuse drives, check S.M.A.R.T. data and run stress tests. Drives with bad sectors or high reallocated sector counts are red flags.
- Fans and cooling: Listen for unusual noises and inspect fan rotors. Replace any that sound unhappy; a failed fan can lead to overheating and data risk.
- RAM and expansion slots: Ensure the RAM is populated to recommended levels and that any PCIe expansion cards (for NICs or storage acceleration) are recognized by DSM.
- Power supply stability: A failing PSU can cause unpredictable reboots and data corruption. If the unit shows instability, factor a PSU replacement into your cost.
- DSM license status: Some DSM features require licenses. In used gear, licenses might be transferable but verify the status before you pay extra for features you think you’ll need.
- Warranty and return policy: If you’re buying from a seller, confirm return windows. DSM is stable, but you want peace of mind if something smells off.

## External Resources and Related Reading
- Synology product page: https://www.synology.com/en-us/products/RS422+
- DSM documentation and feature list: https://www.synology.com/en-us/dsm
- A broader guide to NAS best practices: https://www.synology.com/en-us/blog
- Related Geeknite post: [NAS Storage for Home Labs: Getting Started]({% post_url 2024-03-12-nas-101-getting-started %})
- Related Geeknite post: [RAID-ish Adventures with SHR and RAID 5]({% post_url 2025-11-05-raid-configs-4bay %})

## Practical Setup Walkthrough (What to Expect)
### Step 1: Prep Your Drives
Choose your drives (HDDs for bulk storage, SSDs for cache/fast IO). If you plan to run a media server, consider 4TB or 8TB drives for cost-effective density. For backups and file shares, you might want a mix of space and reliability. Make sure all drives are healthy and formatted to the NAS’s accepted formats.

### Step 2: Install Into the Enclosure
Slide the trays into the 4 bays. The hot-swap trays make it easy to swap in drives without powering down, but you still want to power down before you swap to be safe with hot-swapping in a used chassis. Connect to your network and power up the RS422+. You should be greeted with the DSM splash screen if you did things right.

### Step 3: Create Storage and Users
Within DSM, set up a storage pool and a volume with your preferred RAID layout (SHR is a gentle start for mixed drives). Create user accounts and groups, assign permissions, and set up shared folders. If you’re a security-minded person, enable two-factor authentication and a careful password policy.

### Step 4: Enable Backups, Syncs, and Apps
Install essential packages: Cloud Sync to backup to a remote location or cloud, Drive to mount network shares for collaboration, and Plex or Video Station if you want media serving. If you’re ambitious, you can run Docker containers on DSM to host tiny apps or services—just don’t overfit the CPU and RAM.

## Final Recommendation and Who Should Buy
- The RS422+ is a sturdy, rack-friendly four-bay NAS enclosure that’s a decent pick for a home-lab enthusiast or a small office starting point. If you’re okay with the realities of used gear (potential noise, uncertain warranty, and the occasional mystery hardware quirk), this chassis gives you a solid base to build a flexible storage and backup solution around.
- It’s not the cheapest new-out-the-box option, but the value comes from a dramatic reduction in cost relative to a brand-new enterprise-class NAS and the satisfaction of a DIY upgrade path. You’ll learn more about RAID, DSM, and network topology in one week than most people do in a year of “plug and pray” storage purchases.
- If your throughput needs and reliability concerns are modest, the RS422+ is a good starting point that you can scale from with PCIe NICs and additional drives down the line. The combination of a 4-bay chassis and Synology’s DSM ecosystem provides a lot of bang for the buck, especially when bought used and properly maintained.

### Quick Summary
- Pros: Rack-ready, four bays, scalable NIC options via PCIe, DSM’s robust app ecosystem, flexible RAID options, good for backups and small-scale file sharing.
- Cons: Used gear may have noisy fans, variable warranty, potential unknowns around drive health, and you’ll need to couple with drives (and possibly a PCIe NIC) to reach your desired network throughput.
- Who should buy: Home lab enthusiasts, hobbyists, small offices needing a centralized file server and backups, and anyone who appreciates a good deal on a rackmount NAS chassis.

## Final Verdict
If you’re scouting a used Synology RS422+ for a 4-bay NAS enclosure, you’re basically trading a bit of insurance for a lot of flexibility. It’s not a “set it and forget it” gadget; it asks you to make thoughtful choices about drives, RAID, network topology, and DSM apps. But when you do, you’ll have a compact, rack-friendly, feature-rich platform that can handle backups, file sharing, media serving, and more—with the friendly Synology DSM aesthetic guiding you through the labyrinth.

So yes, this RS422+ can be a strong foundation for a home-lab or a small office, provided you go in with eyes open, your drives are healthy, and your expectations are tuned to the realities of used gear. If you’re patient, you’ll end up with a reliable, capable NAS that makes your data feel deservedly pampered.

**Bottom line: For a tidy 2U, 4-bay, used NAS that plays nicely with DSM and your network, the RS422+ is a surprisingly decent choice—so go ahead and grab one if the price is right and you’re ready to assemble the pieces.**

**Affiliate Note: Ready to turn this into a reality? Buy through our partner link and support Geeknite at the same time: https://affiliate.geeknite.example/rs422-plus**