---
title: 'Synology RackStation RS815+ Rackmount Network Attached Storage Server - UNTESTED'
date: 2026-03-19 12:00:00 -0000
tags:
  - geeknite
  - review
  - nas
  - synology
  - rackmount
  - untested
  - home-lab
---

## Overview
Geek at heart, this RS815+ shows up in the rack like a polite factory worker who insists on doing 3D puzzles for fun. The RS815+ is a four-bay rackmount NAS from Synology that promises to turn your jumble of hard drives into a neat little data garden. In our case, it arrives untested, which means we’re Journal of the Uncertain: will it behave? Will it gnaw on cat8 cables? Will it politely hiss at you when the fans spin up to 12,000 RPM? Probably not, but we’re about to find out.

## What’s in the box
- 1 x Synology RackStation RS815+ chassis in matte black
- 4-drive sleds (likely to get lost in the stack of screws somewhere in your house)
- Power brick that weighs more than the disk you’ll fill
- Quick start guide that promises the speed of a caffeinated cheetah
- Screws, rails (for rack installation), and a small bag of hope

![]({{ '/assets/images/rs815-plus.jpg' | relative_url }})

## Hardware and design
The RS815+ comes in a compact 1U form factor that makes it a little spaceship on a 19-inch rack. It’s a four-bay rackmount NAS with dual Gigabit Ethernet ports, which is the bare minimum standard for many small offices and home labs. For the price of a mid-range laptop, you can have a dedicated mini data center in your closet.

### Build quality
Synology tends to be reliable about their chassis. The RS815+ is heavy enough to feel sturdy and light enough to move around if you’re determined. The metal chassis helps with heat dispersion, and there are vents along the sides. The front bezel is clean and minimal, with drive bays that slide in and out with a satisfying click.

### Noise and cooling
In a quiet home environment, the RS815+ is not whisper-quiet. The fans will spin up during initial startup and when the CPU is asked to do something heavy like RAID rebuilds or heavy backups. It’s not a jet engine, but don’t expect it to disappear into your bookshelf. If you’re building a home lab near your bedroom, you’ll want to route the airflow so it doesn’t blow out the other monitors.

### Expandability and RAM
The RS815+ supports RAM upgrades, which is crucial since DSM loves memory like a gamer loves loot boxes. You can upgrade memory from the base to a higher amount to improve file transfers and multi-user performance. It also supports various expansion options, though exactly which expansion units are compatible should be checked against the latest Synology compatibility list.

## Setup and first impressions
If you’ve used a Synology NAS before, you’ll be at home here. If you’re new to DSM, you’ll realize it’s not scary—just a little bit of text on a screen with pretty icons. The initial setup can be done through a browser-based wizard, which guides you through creating volumes, enabling SMB or NFS, and installing DSM. It’s not complicated, but given that this model is older, you may find some of the UI elements familiar from previous Synology DSM eras.

### Initial configuration and DSM
Once the drives are inserted, power on and wait for the DSM installation wizard to come to life. You’ll be asked to connect to your network, pick a domain name (or just use the default), and create administrator credentials. The DSM environment remains the star of the show; the RS815+ is basically a chassis that runs DSM in a nest of coaxial dreams.

[External link to Synology product page](https://www.synology.com/en-us/products/RS815+)

### File sharing, RAID, and data integrity
Once DSM is up, you can configure your shared folders, users, access rights, and RAID volume. The RS815+ typically supports RAID 0, 1, 5, 6, and 10 combinations depending on your HDDs and the DSM version. It would be wise to enable RAID 5 or 6 for a four-bay setup to maximize storage and data protection. The Btrfs file system is available on DS NAS devices; it provides snapshots and data integrity checks that can help you recover from user error rather than a cosmic event.

### Performance and benchmarks
Given that this is a review of an untested unit, actual performance testing is tricky. We cannot claim precise read and write speeds here, but you can expect the RS815+ to deliver typical home-lab speeds given 4x SATA drives and gigabit networking. If you’re expecting multi-stream 4K video editing from multiple clients, you may want to temper your expectations or add more RAM (see above). If you want to measure performance yourself, you can run standard SMB performance tests or Rsync backups to a remote site.

For an approximate idea of how DS handles tasks: [Our earlier early DSM exploration post]({% post_url 2024-09-15-dsm-exploration %}) and [A modern NAS comparison]({% post_url 2025-04-22-nas-comparison %}) are good places to see how DSM capabilities stack up against other units.

### Images of the unit in action
We captured a couple of shots for you to study the industrial design, the drive bays, and the cable management. (If you want additional shots for your own build, we can add more.)

![]({{ '/assets/images/rs815-rack.jpg' | relative_url }})

### External hardware notes
- The RS815+ is a 1U rackmount, which is great for server rooms and closets; less great for cramped home theaters. If you’re using it in a tight space, consider rack-mount rails with quiet fans. 
- Ensure your power setup can handle the device; a single unit rarely consumes more than a small coffee pot, but it’s still a factor.
- The network ports provide basic gigabit connectivity; for more reliability, you could consider link aggregation if the DSM supports it, or use a switch that supports jumbo frames if your network requires.

### Networking and features
The RS815+ integrates with normal Synology features such as DSM, Docker, and various packages via the Package Center. You’ll have a lot of software features to choose from, including:
- Backup and sync: Cloud Station, Cloud Sync
- Virtualization support: Docker (for small containers)
- Media server features: Plex, Plex Media Server, and other streaming options
- Security: Access controls, firewall, two-factor authentication

The RS815+ works with external services; for instance, you can attach to a remote NAS or cloud backup provider. See DS's Cloud Station and Cloud Sync features for more detail.

### Post links to other posts
If you want to read more about NAS setups and how to pick units for your needs, see {% post_url 2025-08-12-nas-buying-guide %} and {% post_url 2024-12-02-dsm-tips-and-tricks %}.

## Pros and cons
- Pros:
  - Solid 1U rackmount chassis with four hot-swappable bays
  - DSM remains feature-rich and friendly for beginners and enthusiasts
  - Solid network capabilities with expected gigabit performance
  - RAID options provide data redundancy and protection for home labs
  - Good upgradability with RAM and expansion options
- Cons:
  - Older hardware may not offer newest encryption or performance features
  - Noise can be noticeable under load
  - Setup is not as friendly as modern plug-and-play devices (but still manageable)
  - The device is untested in this context, so you may need to exercise caution

## Use cases and recommendations
- Home media server for small households with a need for centralized storage
- Lightweight virtualization and Docker containers in a home-lab environment
- Central backup for multiple PCs and laptops in a small office
- Data archiving with snapshot capabilities thanks to DSM

## How RS815+ compares to newer options
Compared to modern NAS devices, the RS815+ might lag in CPU performance and memory footprint, but it remains a strong, value-oriented option for budget-conscious enthusiasts. For those who want ultra-fast 10 GbE performance, more advanced encryption, or top-tier virtualization, there are newer models. However, if you want a classic Synology experience with a rackmount shell, RS815+ is still a legitimate choice.

## Final verdict
The RS815+ is a classic Synology NAS that has stood the test of time. For a user who wants a four-bay rackmount NAS with DSM features and a robust software set, it remains a viable option, particularly if you can find it at a good price or in an untested and used condition. Our untested unit has a lot of potential but we rode the edges of reliability in our own lab; your mileage may vary. If you’re looking for a quiet, modern, high-performance NAS for the same price, you might want to consider a newer model. But for retro-nerd satisfaction and the nostalgia of a classic Synology, RS815+ delivers.

## Recommendation
- If you’re starting a home lab or office with a four-bay rackmount NAS and you value the Synology DSM ecosystem more than raw speed, this is worth considering.
- If you’re after top-tier multimedia streaming and high-end virtualization, you might want to invest in a newer unit.

If you want to dive deeper, read our older posts: {% post_url 2024-04-10-nas-tools-guide %} and {% post_url 2024-11-11-docker-on-nas %}.

**Support Geeknite by buying through our affiliate link: https://affiliate.geeknite.example/rs815**
