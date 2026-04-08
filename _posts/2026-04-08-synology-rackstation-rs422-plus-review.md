---
title: Synology RackStation RS422+ 4-Bay NAS Enclosure (No Drives) — Used Verdict
date: 2026-04-08
tags:
  - NAS
  - Synology
  - Rackmount
  - UsedGear
  - HomeLab
  - Geeknite
---

## Introduction
In Geeknite terms, a rackmount NAS is the grown-up version of a home server: louder, heavier, and with more LEDs to pretend you know what you're doing. The Synology RackStation RS422+ is a four-bay chassis designed to sit in a network rack, humming away while you pretend to be a sysadmin. Today we're reviewing a used, drive-less RS422+ that traveled back from a small IT closet, probably wearing a mask that says, I survived three data-center migrations and a sale at a thrift store. We'll explore what you get when you buy used, whether it's worth the swing, and how it stacks up against the more modern, shiny boxes that arrive with a sticky note that reads plug and play. Spoiler: it's still pretty darn capable, especially if you're assembling a budget-friendly rack for a home lab or a small business.

## Unboxing and First Impressions
Wait, it arrives as a bare skeleton? Yup. The RS422+ is sold without drives, and in the used market you might get it in a plain brown box with more dust than a minimum wage inventor's hat. The chassis is a solid metal 2U rackmount with four drive bays at the front, hot-swappable trays, and a front panel that looks like it could double as a spaceship console if you squint hard enough. The build quality feels sturdy, with metal rails that slide smoothly and a front that says, I mean business, but I also come with built-in fan noise that will remind you of a small jet engine. One of the benefits of a used RS422+ is you can snag a premium rack solution for a fraction of the new price, provided you do your due diligence: check fans for wobble, listen for grinding, and verify that the DSM OS is present on the unit (or at least can be reinstalled).

{% image assets/rs422_plus.jpg alt=Synology RS422+ 4-Bay NAS Enclosure in rack %}

In the wild, you will see the RS422+ deployed in small offices, media studios, and ambitious home-lab setups. It is designed to be rack-mounted, with four drive bays that can house 3.5" or 2.5" drives depending on trays. The unit may ship with pre-installed fans and a power supply that makes noise as if it’s running a marathon in a data center. If you’re buying used, ask about the fan condition, the presence of any warning codes during boot, and whether the DSM OS is present on the unit (or at least can be reinstalled). The price-to-performance ratio for a used RS422+ is appealing if you’re comfortable with a bit of mechanical age and a learning curve. For many geeks, this is the perfect budget rack gateway to the world of rack-mounted storage without committing to an modern 2U, 16-bay beast that costs more than a used car.

External link: Synology product page: https://www.synology.com/en-us/products/RS422+

If you want to compare to other Synology rackmounts, check our older post: {% post_url 2024-06-12-synology-rackstation-comparisons %}.

If you want to know what a modern DSM can do in a budget scenario, see our DSM overview post: {% post_url 2025-08-14-synology-dsm-overview %}.

## Design, Build, and Ports
The RS422+ presents a professional silhouette: two rows of drive bays on the front, a slim LCD? Not exactly, but there is a panel with status LEDs that tell you volume health at a glance and if the disk pack is healthy. The chassis is designed to be scrappy, but sturdy enough to survive in a rack with occasional dust storms (or the occasional sneeze from a colleague who forgot to mute their mic during a video call). The four bays use standard drive trays that you can swap without tearing the entire unit apart. The rear houses the power supply and cooling fans. The fans are not silent; they're not the loudest thing in your home theater equipment either, but expect a whirr that is noticeable in a quiet room. If you run a home lab in a closet or spare room, the RS422+ can be a pleasantly unobtrusive presence when matched with proper ventilation.

{% image assets/rs422_plus_front.jpg alt=Synology RS422+ front panel %}

In terms of brandless performance, the RS422+ runs DSM, Synology's DiskStation Manager OS. DSM provides an intuitive web interface for managing volumes, users, and services. Having a 2U form factor and a rackmount design makes it perfect for offices or labs that need rack-based storage without the cost of enterprise-grade hardware. The OS comes with robust features: snapshots, file syncing, remote replication, and a library of apps for surveillance, media streaming, and backup. It’s not just a box that stores files; it’s a pocket-sized data center.

## Setup and First Boot Experience
First boot on a used RS422+ is a mixed bag: if it comes with a clean DSM installation, you’re in luck; if not, you’ll need to install DSM from Synology’s knowledge base. The installation process happens via a web interface, typically accessed by connecting to the device’s IP address and running the DSM setup wizard. The process is straightforward for anyone who has previously installed a NAS or a home router, which should cover a large portion of geeks and IT hobbyists.

For initial setup, you’ll want to:
- Assign a management IP address or enable DHCP and then reserve an IP in your router.
- Create admin credentials with a strong password and enable 2FA if available.
- Configure your storage: create a volume, then set up an appropriate RAID type: SHR (Synology Hybrid RAID) if you want a flexible approach to drive sizes, or a classic RAID for predictability.
- Enable essential services: SMB for Windows/macOS file sharing, NFS for Linux clients, and perhaps rsync for backups or replication to a remote site.
- Ensure backups for your own files. For many geeks, a well-structured backup plan is more important than any speed benchmark.

If you want to see a more detailed step-by-step, check out our post on setting up a similar Synology NAS: {% post_url 2025-03-28-step-by-step-nas-setup %}.

Look for the status indicators on the front panel during boot. If you see a warning light, you’ll want to consult the logs to determine if a drive or a port is failing. In a used RS422+, that could be a sign of fan wear or an aging power supply, so approach the first boot as a sanity check rather than a celebration.

## Performance and Real-World Usage
In real-world usage, the RS422+ behaves differently depending on the network and the drives inserted into the bays. If you’re streaming 4K video from the NAS to multiple clients at once, your results will heavily depend on the network bandwidth and the drives used. In most home-lab scenarios, you’ll likely see sustained throughput in the 100-140 MB/s range over a single gigabit network, which is perfectly adequate for file sharing, backups, and light virtualization testing. If you have 2.5GbE or 10GbE networking, speeds can improve and allow for more robust multimedia streaming or faster backups to/from your PC.

For iSCSI targets or virtualization labs, you can tune performance through the DSM interface by enabling iSCSI targets or by deploying the NAS as a VM host for light workloads. We tested with a mix of 4 TB and 8 TB drives across the four bays, giving a balanced combination of capacity and reliability. RAID 5/6 shrinks usable space compared to RAID 0, but provides fault tolerance. In a storage-heavy use case, you can rely on Synology's software features like snapshots to recover earlier versions of files, even if a drive goes offline.

You might want to consider USB-based external drives as a temporary scratch pool when migrating data to your four bays. The RS422+ does offer USB ports for external backups and service booting, albeit at USB 3.0 speeds rather than USB-C or Thunderbolt. As always, the speed of any storage device is only as good as the slowest link in the chain, so plan accordingly.

A quick comparison with a modern 4-bay rackmount from a different vendor shows that the RS422+ holds its own in terms of reliability and practical features. It may not have the latest hardware acceleration or the hottest NVMe caching options, but DSM invests in features that make a NAS helpful for everyday tasks: automated backups, centralized media libraries, and easy collaboration with other devices on the network. If you're migrating from a consumer NAS or building a small office storage system, the RS422+ provides a familiar interface and a robust feature set that will carry you through a few upgrades.

For a deeper sense of DSM features and their capabilities, see our post on the DSM ecosystem: {% post_url 2025-08-14-synology-dsm-overview %}. Also, for practical network storage tips, check our rack NAS guide: {% post_url 2024-06-01-rack-mounted-nas-guide %}.

## Data Protection, Security, and Reliability
The RS422+ supports common security features such as user authentication, access control, and encrypted communication for clients that mount shares. With four bays, you have the freedom to choose your preferred RAID layout, balancing capacity and redundancy. A crucial aspect of used gear is to verify that the unit has not suffered from repeated power cycles without a proper shutdown; this can wear on the PSU and fans. Periodic maintenance in a used unit can help maintain reliability if your goal is a long-running NAS for a home lab or small office.

Synology DSM also brings features like:
- Snapshots to protect against accidental deletion or ransomware.
- Local and remote replication to another NAS or to a cloud service.
- Active backup and scheduling for computers and servers in your network.
- Surveillance Station, should you have cameras in your environment; you can deploy a modest DVR-like setup from the RS422+ if you want to watch the security logs.

In our tests, the RS422+ performed reliably for daily tasks such as file sharing, backups, and streaming. It’s a comfortable middle ground for a rackmount that doesn’t veer into enterprise-grade complexity. And if you want to dive deeper into NVR and surveillance features, you can refer to our post on Synology surveillance compatibility: {% post_url 2024-11-29-surveillance-station-overview %}.

## Use Cases: Who Should Consider the RS422+?
- Small offices needing centralized storage for backups and shared files.
- Home labs where you want a rack-mount companion for experimenting with virtualization, Docker, and network services.
- Media centers that want centralized streaming to multiple devices with a robust, dependable storage backend.
- Enthusiasts who want a gear-piece to display in a server rack and the satisfaction of hearing the fans whirr.

The 4-bay design provides ample room for future expansion, especially if you expand your drive sizes gradually rather than upgrading the NAS. The ability to configure SHR ensures you can mix and match drives of different sizes without letting go of the dream of a flexible RAID configuration. If you plan to run multiple services on the NAS, DSM's ability to host packages like a media server, a VPN server, or a cloud sync client can help you consolidate devices and reduce clutter.

## Used Gear Considerations and Caveats
With used gear, your biggest risk is the wear and tear that comes with years of operation:
- Fans: Louder than modern quiet boxes; consider replacing or spacing to reduce noise. If you’re deploying it in a living room or bedroom, you might want to implement a sound-dampening approach.
- Power supply: Aging PSUs can fail; inspect the unit for any unusual heat or burning smells. Have a backup plan and a plan to replace it if needed.
- Firmware and DSM: Ensure that the DSM can be reinstalled and updated to a supported version. If you can’t boot cleanly, you’ll need to source the proper installation images and license keys.
- Drive bays: If the unit ships without drives, you obviously must add them. But if the seller used the unit with old drives, you risk carrying away data that’s not yours; a full wipe of the drives is recommended when installing your own drives.

Pro tip: if you’re buying used, request the drive trays and screws, check the rails for corrosion, and ensure the unit has a clean boot environment before purchase. You can also ask for a pre-boot health check to reassure yourself about the fan and PSU health.

## Alternatives and Comparisons
If you’re still on the fence after reading this, there are several alternative rackmount options you might consider:
- A newer 4-bay rack NAS with newer CPUs and energy-efficient designs.
- A 2U, 8-bay rack NAS if you need more capacity and room for expansion.
- A dedicated small-business backup appliance, if you’re not interested in virtualization, but want the strongest data protection.

For folks who are curious about how the RS422+ stacks up to more modern alternatives, our guides offer more context: see the following posts for deeper dives:
- Rack-mounted NAS buy guide: {% post_url 2024-06-01-rack-mounted-nas-guide %}
- Synology DSM overview: {% post_url 2025-08-14-synology-dsm-overview %}

## Final Verdict: Should You Buy a Used RS422+?
If you’re on a budget, want a rack-mounted four-bay NAS, and are comfortable with a unit that has been previously used, the RS422+ is a strong candidate. It provides a robust DSM experience, a rack-ready design, and the performance parity you’d expect from a NAS in its class, with the caveat that used gear needs maintenance. It’s particularly appealing for home labs or small offices where you want to set up a dedicated storage appliance without paying top-tier enterprise prices. If you’re new to NAS devices, this could be a good stepping stone; it’s not too complex, but it’s a real device that can host a lot of services and data.

However, if you need extreme performance, the ability to host multiple VMs on the device, or you want the latest hardware with abundant RAM for heavy virtualization workloads, you might be better off stepping up to a newer platform. It’s not a bad alternative to the hot, new appliances; it’s a sane, proven solution that will likely outlast a consumer-grade NAS and provide a stable home base for your files and services.

For a final round-up and more context about pricing, check how this NAS stacks up against other gear in our rack NAS price guide: {% post_url 2025-03-01-rack-nas-price-guide %}.

## What’s the Geeknite Recommendation?
- Buy if you want a budget-friendly, rack-ready four-bay NAS for a home lab or small office with the caveat that used gear can be variable; verify the fan health and the power supply, ensure you can reinstall DSM, and be prepared to replace components as needed.
- Don’t buy if you require the latest hardware, silent operation, or you need many virtualization features. In that case, consider a newer rackmount NAS or a dedicated server with a more flexible upgrade path.

Overall, the RS422+ is a practical, reliable, and sensible choice for readers who want a rack-friendly NAS that does not break the bank. It’s not glamorous, but it’s like a dependable friend who helps you back up your life and never complains about the size of your media library.

If you’re ready to dive into the RS422+ or want to show off your own used gear story, you can check our shop page for more resources and gear deals: https://geeknite-store.example.com/rs422plus

**Buy the RS422+ through our affiliate link and help support Geeknite at the same time: https://geeknite.com/affiliates/synology-rs422+**
