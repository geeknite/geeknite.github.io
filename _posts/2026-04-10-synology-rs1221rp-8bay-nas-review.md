---
title: Synology RackStation RS1221RP+ 8-Bay NAS Review
date: 2026-04-10
tags:
  - NAS
  - Synology
  - RS1221RP+
  - 8-Bay
  - Rackmount
  - 8GB RAM
  - HDD
---

## Overview
Welcome to Geeknite's lab, where we wrangle data centers into tidy little bundles you can tuck into a closet and pretend is a legitimate IT department. Today we tackle the Synology RackStation RS1221RP+ 8-Bay NAS, a rack-mount monster that comes with 8 GB of RAM, rack ears, and, as shipped in this test kit, a pair of 8 TB Seagate hard drives ready to spin out some data drama. If you ever wondered how to convert a quiet closet into a functioning mini data center for a home office or small business, this is your ticket. It looks like it belongs next to the network switch and the UPS in a rack, and it behaves like it means business without needing a coffee break every five minutes.

This review sticks to the kit we received—two 8 TB Seagate HDDs, 8 GB RAM installed, rack ears included—while testing drive performance, DSM features, expandability, and long-term reliability. The RS1221RP+ sits in Synology's RackStation lineup and is designed for people who want serious storage in a compact, rack-mount package. It’s not a toy; it’s a grown-up storage appliance with the DSM operating system offering a gauntlet of features that makes backups, virtualization, media serving, and collaboration feel like you’re running a tiny enterprise from a padded closet.

The big question: is this the right starting point for your data hoard, or should you wait for a different model or a larger budget? We’re going to unwrap the hardware, test the software, and weigh the pros and cons so you can decide if the RS1221RP+ belongs in your rack or in a distant dream of better data resilience.

### What's in this kit
In this test box you’ll typically find the RS1221RP+ chassis with the eight drive bays, two plastic rack ears for 19-inch equipment racks, a power cable, and mounting screws for 3.5-inch drives. The two 8 TB Seagate HDDs are installed on hot-swappable trays, so you can remove, swap, or upgrade drives without tearing the rest of your rack apart. The whole package is designed to reduce the friction between “I want a capable NAS” and “I want to actually use it without a degree in IT administration.”

For those who like to see the hardware specs in plain language:
- 8 bays for hard drives (hot-swappable)
- Rack-mountable 2U form factor
- 8 GB RAM in this test kit (upgrade path varies by model)
- Rack ears included for mounting in a standard 19-inch rack
- Two preinstalled 8 TB Seagate HDDs
- DSM operating system with a strong emphasis on data protection, virtualization, and collaboration features

If you want to geek out further, you can check the official page for more specifications and expansion options: [Synology RS1221RP+ official page](https://www.synology.com/en-us/products/RS1221RP+).

And for readers who like to compare notes, see our related posts: [RS820+ Review]({% post_url rs820-plus-review %}) and [DSM 7.2 Features Deep Dive]({% post_url dsm-7-2-features %}).

### Design and build quality
The RS1221RP+ ships as a solid, no-nonsense rackable chassis. Metal construction, clean lines, and a front that is friendly to drive trays and indicators rather than a glossy vanity mirror. The eight drive bays on the front are straightforward: you pop trays out, replace drives, and slide them back in. The indicators give you at-a-glance health and access status, which is handy during a long backup window when you don’t want to wake the neighbors while checking LED patterns.

Mounting it in a rack is a delight for those who enjoy the “all the IT gear in one place” aesthetic. The included rack ears are sturdy and attach with standard hardware, so you’re not fighting awkward brackets or improvised mounts. If you’re already stocking a rack with switches and a patch panel, the RS1221RP+ sits in line with the rest of your gear, whispering the subtle promise of data safety rather than shouting about it.

The interior layout prioritizes serviceability. Hot-swappable trays mean you aren’t tearing the entire enclosure apart to replace a stubborn disk. The included cooling solution keeps the internal temperatures in check under typical loads. It’s not a silent device—rack gear has fans, and the fans do their job—but it’s not loud enough to disturb casual office chatter unless you push it into a full-bore I/O sprint.

### Drives included: two 8 TB Seagate HDDs
In this kit you get two 8 TB Seagate hard drives—enough to get you started with a big chunk of storage out of the box. Seagate drives are a common choice for NAS systems thanks to their reliability and endurance under sustained workloads. With 16 TB raw capacity in the box, you can set up RAID 0 for raw performance (not recommended for data safety), RAID 1 for mirrored redundancy, or SHR (Synology Hybrid RAID) to adapt as you add more disks later. The dual-drive starting point is a practical way to get into RAID experimentation without waiting for the rest of your budget to appear from the ether.

If you’re planning to grow, the RS1221RP+ supports expansion units for more bays. You can expand storage without moving to a bigger chassis, which is handy if your data footprint grows faster than your ambition. The expansion path is a feature many small businesses rely on when their data needs scale beyond eight disks.

### Disk management and file systems
Synology DSM handles disks with a thoughtful approach to reliability. With Btrfs in DSM, you get features like data checksums, point-in-time snapshots, and efficient data integrity protection. If you’re primarily backing up media or documents, snapshots let you roll back to a known good state after a messy ransomware scare or the occasional human error in a shared folder.

The default file systems and configurations can be tailored to your needs. If you’re a power user, you’ll appreciate the option to configure S.M.A.R.T. tests, drive health checks, and automated scrubbing tasks. If you’re new to NAS ownership, DSM makes the complexity manageable with guided setup wizards and sane defaults.

### Setup and the DSM experience
Setting up the RS1221RP+ is pleasantly straightforward. Connect the unit to power, connect it to your network, and power it up. DSM’s Quick Setup wizard guides you through basic tasks: naming the NAS, enabling DSM updates, creating user accounts, and configuring shared folders. If you’re migrating from another NAS or a Windows shared folder, there are built-in tools to help you move data with minimal drama.

The web-based DSM interface is where Synology earns both respect and a few certificates of nerd-cred. It’s clean, logical, and full of helpful wizards. Security is front and center, with options for Two-Factor Authentication, passphrase policies, and IP-block lists. You can tailor DSM to your environment—from a home media server that streams 4K content to a backup target for a fleet of laptops and workstations.

Security is not just about the interface; it’s about patterns. The RS1221RP+ thrives in a backup-heavy workflow: weekly snapshot routines, offsite replication with another NAS, and the ability to configure cloud backups. The DSM ecosystem isn’t perfect, but it’s among the strongest in the consumer-pro and small-business NAS space, with a robust app catalog that lets you run Docker containers, virtual machines, and a host of community-driven packages.

### Performance and networking expectations
With 8 GB of RAM, the RS1221RP+ handles a handful of simultaneous users and workloads without getting fussy. In a typical small-office scenario, you’ll be serving files to laptops, media players, and a handful of virtualization tasks. Real-world throughput depends heavily on disk health, network bandwidth, and whether you’re using RAID for redundancy or speed. On a standard Gigabit network, you’ll often see sustained transfer rates in the 100–140 MB/s range under moderate load when using efficient protocols and caching. If you’re lucky enough to have a 2.5 GbE or 10 GbE link (or use link aggregation), you’ll see higher sustained throughput, particularly for sequential transfers and backup tasks.

 RAM matters here. 8 GB is a practical baseline for a NAS intended to host multiple services: file sharing, automated backups, a small virtual machine, perhaps a Docker-based app suite. If your workload includes lots of virtualization or heavy container workloads, you’ll want to look at a memory upgrade path or a model with more RAM from the start, because DSM loves memory for caching and pool management. (As with all things virtualization, your mileage may vary based on workload type and number of VMs.)

### RAID options, data safety, and capacity planning
RAID and data protection are central to NAS planning. The RS1221RP+ supports standard Synology RAID options in DSM, including SHR for easy drive replacement and capacity optimization, traditional RAID 5/6 when you have more than two drives in the mix, and mirrored configurations for redundancy. With two drives on day one, you’ll likely run either a two-disk SHR setup or a RAID 1 mirror if you want simple redundancy. As you add drives, RAID 5 or 6 can offer a comfortable balance of capacity and fault tolerance.

With eight bays, your capacity planning becomes more interesting. You’ll be tempted to populate the box with eight 8 TB drives in a large RAID for a huge pool of storage. Then the next temptation hits: you realize you could run a mixed configuration to prioritize performance for VM storage, while keeping some drives for backups of critical servers. This is where DSM shines—the flexibility of SHR means you can start lean and grow without reformatting or starting from scratch.

### Use cases: who benefits most
- Small business backup hub: centralize backups from laptops, desktops, and servers, with scheduled snapshots and offsite replication.
- Office media server: stream media to NAS-connected TVs and media players, while keeping a robust catalog of media files and metadata.
- Lightweight virtualization: host a few Docker containers or lightweight VMs for testing software, labs, or demos without burning through your workstation’s RAM.
- Data hoarder with room to spare: eight bays means you can keep project archives, photos, and design assets without shrinking into a single drive pool that’s one backup away from disaster.

### Performance notes and caveats
- Expect solid performance for typical NAS tasks, with capacity to scale as you add more drives.
- If you expect intense virtualization or large VM workloads, consider more RAM or a higher-end model—RAM is the quiet hero of NAS performance.
- Drive health and firmware updates matter. Always keep drives up to date and run SMART tests on a schedule that fits your risk tolerance.
- For best results, ensure you have a fast network path; use modern switches and consider higher-speed links if your budget allows.

### Pros and cons at a glance
Pros:
- Eight bays in a compact rack-mount form factor
- Rack ears included for easy mounting in a 19-inch rack
- DSM offers a robust, user-friendly ecosystem with strong data protection features
- Preinstalled drives give you an immediate starting point
- Good balance of performance, features, and expandability

Cons:
- 8 GB RAM may feel tight for heavy virtualization workloads unless you upgrade
- Rack-style NAS means it’s physically larger than desktop units, which may matter in smaller closets
- Two drives at launch means you’ll want to upgrade for meaningful large-scale RAID configurations

### Final verdict and who should consider it
If you’re looking for a solid, rack-mountable NAS that blends enterprise features with consumer-friendly usability, the RS1221RP+ is a strong candidate. The combination of eight bays, rack mounting convenience, and DSM’s feature set makes it particularly attractive for small offices, creative studios, and serious home labs that want to centralize backups, media serving, and lightweight virtualization in one polished package. The included 8 GB RAM is a sane starting point for most tasks; you’ll appreciate the headroom as your workloads scale, or you’ll love the option to expand memory if your NAS supports it. The included Seagate drives are a practical starting point, though you’ll want to plan for additional drives if you want larger storage pools, higher redundancy, or more aggressive backup schedules.

Bottom line: the RS1221RP+ with 8 GB RAM and two 8 TB Seagate drives is a commendable entry into rack-mounted NAS territory. It’s not the cheapest option you’ll find, but it delivers a compelling mix of reliability, expandability, and software power that you’ll actually use rather than just admire from afar.

### Recommendations for buyers
- If your data needs are growing and you want a rack-mount solution that scales with you, this is a solid starting point.
- Plan for at least a few additional drives to take full advantage of RAID options and capacity growth.
- Invest time in configuring snapshots and offsite replication for real-world data protection.
- If virtualization or heavy container workloads are on the menu, budget for extra RAM or consider a higher-end model to avoid swapping to disk under load.

## External resources and related posts
- Synology official RS1221RP+ page: [Synology RS1221RP+](https://www.synology.com/en-us/products/RS1221RP+)
- Explore related posts: [RS820+ Review]({% post_url rs820-plus-review %}) and [DSM 7.2 Features Deep Dive]({% post_url dsm-7-2-features %})

## Visuals in the lab

![](/images/rs1221rp-front.jpg)

![](/images/rs1221rp-drive-trays.jpg)

![](/images/rs1221rp-dsm-screenshot.jpg)

### Why Geeknite loves this setup
- The rack ears are a real sanity saver for closet-based data centers.
- The eight bays give you room to experiment with different RAID layouts and data protection strategies.
- DSM makes backup, virtualization, and file sharing approachable without turning your life into a tech manual.
- The kit is practical for real-world usage, not just a showroom display piece.

## Final recommendation and call to action
If your goal is a capable, scalable, rack-mount NAS that can host backups, media, and light virtualization while still fitting into a professional-looking rack, the Synology RS1221RP+ with 8 GB RAM and two 8 TB Seagate drives is a smart pick. It balances expandability with a user-friendly software stack, giving you a solid foundation for a small office or serious home lab. The best path is to start with this kit and grow as your data needs expand, adding more drives and RAM as your workload requires.

**Get it now via our affiliate link and support Geeknite as you build your tiny data empire:** https://geeknite.com/affiliate/synology-rs1221rp
