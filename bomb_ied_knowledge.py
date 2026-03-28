
# -*- coding: utf-8 -*-
"""
Bomb & IED Knowledge Base
Source: Bangladesh Army BIDC Book 2023 + IED & CBRN Book
বাংলাদেশ সেনাবাহিনীর রেফারেন্স বই থেকে তথ্য
"""

BOMB_IED_KNOWLEDGE = {
    'bn': {
        'chapters': [
            {
                'id': 'ch1',
                'title': 'বিস্ফোরকের সংজ্ঞা ও প্রকারভেদ',
                'source': 'বিআইডিসি বই-২০২৩, অধ্যায়-১',
                'content': """
## বিস্ফোরক (Explosive)

**সংজ্ঞা:** বিস্ফোরক হলো কঠিন অথবা তরল অথবা বিভিন্ন পদার্থের অস্থায়ী সংমিশ্রণ যাহা প্রয়োজনীয় উদ্দীপকের উপস্থিতিতে অতি আংশিক অথবা সম্পূর্ণরূপে স্থায়ী বায়বীয় পদার্থে রূপান্তরিত হইয়া বিপুল পরিমাণ তাপ ও চাপের সৃষ্টি করে কোনো বস্তুকে আংশিক বা সম্পূর্ণরূপে ধ্বংস করে।
*(সূত্র: বিআইডিসি বই-২০২৩)*

## বিস্ফোরকের প্রকারভেদ

### ১. ক্ষমতা বা শক্তির উপর ভিত্তি করে

**ক) উচ্চমাত্রার বিস্ফোরক (High Explosive):**
উচ্চ ক্ষমতাসম্পন্ন বিস্ফোরক, কিন্তু ইনিশিয়েটিং বিস্ফোরক হইতে কম স্পর্শকাতর বা সেন্সেটিভ। সঠিক মাত্রার ডেটোনেশন ওয়েভ পাইলে ইহা বিস্ফোরিত হয়।

উদাহরণ: হেক্সোজেন, পিই, টি.এন.টি ইত্যাদি।

উচ্চমাত্রার বিস্ফোরক দুই প্রকার:
- **(১) প্রাইমারি হাই এক্সপ্লোসিভ:** ইনিশিয়েটিং এজেন্ট (Initiating Agent) - সহজে বিস্ফোরিত হয়
- **(২) সেকেন্ডারি হাই এক্সপ্লোসিভ:** বার্স্টিং চার্জ - কম সংবেদনশীল, বেশি শক্তিশালী

**খ) নিম্নমাত্রার বিস্ফোরক (Low Explosive):**
নিম্ন ক্ষমতাসম্পন্ন বিস্ফোরক এবং ইহার উচ্চ স্পর্শকাতরতা বিদ্যমান।

উদাহরণ: গান পাউডার এবং প্রপোলেন্ট চার্জ।

### ২. ব্যবহার হিসেবে বিস্ফোরক তিন শ্রেণিতে বিভক্ত

| শ্রেণি | বর্ণনা |
|--------|---------|
| ইনিশিয়েটর | সর্বপ্রথম বিস্ফোরণ শুরু করে |
| ইন্টারমিডিয়ারিস | মাঝখানে সংযোগ রক্ষা করে |
| বার্স্টিং চার্জ | প্রধান বিস্ফোরক চার্জ |

### ৩. আকৃতি বা বাহ্যিক অবস্থার উপর ভিত্তি করে

- **ক) কঠিন বিস্ফোরক:** টি.এন.টি (TNT)
- **খ) প্লাস্টিক বিস্ফোরক:** ৮০৮, ৮৫১, ৮৫২, ২, ৩, ৩ই
- **গ) তরল বিস্ফোরক:** নাইট্রোগ্লিসারিন (Nitroglycerine)
""",
                'key_terms': {
                    'বিস্ফোরক': 'Explosive',
                    'উচ্চ বিস্ফোরক': 'High Explosive',
                    'নিম্ন বিস্ফোরক': 'Low Explosive',
                    'ডেটোনেশন': 'Detonation',
                    'ইনিশিয়েটর': 'Initiator',
                },
            },
            {
                'id': 'ch2',
                'title': 'বিস্ফোরকের অ্যাকশন ও ইফেক্ট',
                'source': 'বিআইডিসি বই-২০২৩, অধ্যায়-২',
                'content': """
## বিস্ফোরকের ক্রিয়াকলাপ (Action of Explosives)

অনির্দিষ্ট ভর ও আকৃতি বিশিষ্ট কোনো উচ্চ বিস্ফোরক যখন বিস্ফোরিত হয় তখন ডেটোনেশন ওয়েবগুলো তরঙ্গাকারে উদ্দীপনার কেন্দ্র বিন্দু হতে বাহিরের দিকে ক্রমান্বয়ে ছড়িয়ে পড়ে। এই শক ওয়েভ (Shock wave) বা তরঙ্গগুলোর অব্যহতির পর পরই থাকে রি-অ্যাকশন জোন (Reaction Zone)।

## বিস্ফোরকের প্রভাব (Effects)

| প্রভাব | বর্ণনা |
|--------|---------|
| **ব্লাস্ট এফেক্ট** | বায়ু চাপের তরঙ্গ যা আশেপাশের সবকিছু ধ্বংস করে |
| **ফ্র্যাগমেন্টেশন** | ধাতব টুকরো যা উচ্চগতিতে ছুটে যায় |
| **ক্রেটার ইফেক্ট** | ভূমিতে গর্ত সৃষ্টি |
| **তাপীয় প্রভাব** | উচ্চ তাপমাত্রার কারণে আগুন |
| **ভূকম্পন প্রভাব** | মাটির কম্পন |

## বিস্ফোরণের প্রকারভেদ

**১. যান্ত্রিক বিস্ফোরণ:** অত্যাধিক চাপের ফলে যখন কোনো ধারক বস্তুর কাঠামোগত ভাঙন ধরে তখন তাকে যান্ত্রিক বিস্ফোরণ বলে।

**২. রাসায়নিক বিস্ফোরণ:** রাসায়নিক পদার্থের বিক্রিয়ার ফলে সৃষ্ট বিস্ফোরণ।

**৩. সমবেদী ডেটোনেশন (Sympathetic Detonation):** যখন একটি বিস্ফোরক চার্জের বিস্ফোরণের শক ওয়েভ বা ঘাত প্রবাহ নিকটে অবস্থিত অন্য একটি বিস্ফোরক চার্জের বিস্ফোরণ ঘটায় তখন তাকে সমবেদী বিস্ফোরণ বলে।
""",
                'key_terms': {
                    'শক ওয়েভ': 'Shock Wave',
                    'ব্লাস্ট এফেক্ট': 'Blast Effect',
                    'ফ্র্যাগমেন্টেশন': 'Fragmentation',
                    'সমবেদী ডেটোনেশন': 'Sympathetic Detonation',
                },
            },
            {
                'id': 'ch3',
                'title': 'ডেমোলিশনে ব্যবহৃত সরঞ্জামাদি',
                'source': 'বিআইডিসি বই-২০২৩, অধ্যায়-৩',
                'content': """
## ডেমোলিশন সরঞ্জাম

ডেমোলিশন সরঞ্জামকে সাধারণত দুই ভাগে ভাগ করা হয়:

### ক) নন ইলেকট্রিক সরঞ্জাম (Non Electric)

১. **সেফটি ফিউজ নং ১১ মার্ক-২ (Safety Fuze):** ধীরগতির জ্বলন ফিউজ
২. **সেফটি ফিউজ আন্ডার ওয়াটার:** পানির নিচে ব্যবহারযোগ্য
৩. **ফিউজ ইন্সটেন্টিনিয়াস মার্ক-৪:** তাৎক্ষণিক জ্বলন
৪. **এসএফ স্ট্রাইকার (SF Striker):** ঘর্ষণ দ্বারা সক্রিয়
৫. **এসএফ ফ্রিকশন/লাইটার:** হাতে চালিত লাইটার
৬. **ইগনাইটর সেফটি ফিউজ পার্কিউশন মার্ক-৩**
৭. **ফিউজিং ম্যাচ**
৮. **সেফটি ম্যাচ দিয়াশলাই**
৯. **ডেটোনেটর নং ৬, ৮ এবং ২৭**
১০. **প্রাইমার ১ সেমি মি:**
১১. **ডেটোনেটিং কর্ড (Detonating Cord)**
১২. **প্রাইমার সিই/জিসি**
১৩. **চাকু ও ব্লেড**

### খ) ইলেকট্রিক সরঞ্জাম (Electric)

১. **এক্সপ্লোডার বক্স:** বিদ্যুৎ সরবরাহ যন্ত্র
২. **ইলেকট্রিক ডেটোনেটর:** বিদ্যুৎ দিয়ে সক্রিয়
৩. **ওহমস মিটার মডেল ২০৫:** সার্কিট পরীক্ষার যন্ত্র
৪. **ফায়ারিং কেবল:** বিদ্যুৎ বাহী তার

## ডেটোনেটিং কর্ডের ব্যবহার

ডেটোনেটিং কর্ড একটি প্লাস্টিক আবৃত কর্ড যার মধ্যে PETN বিস্ফোরক থাকে। ইহার জ্বলনের গতি প্রতি সেকেন্ডে ৬৫০০ মিটার। এটি দিয়ে একসাথে একাধিক চার্জ বিস্ফোরণ ঘটানো যায়।
""",
                'key_terms': {
                    'সেফটি ফিউজ': 'Safety Fuze',
                    'ডেটোনেটর': 'Detonator',
                    'ডেটোনেটিং কর্ড': 'Detonating Cord',
                    'ইগনাইটর': 'Ignitor',
                    'এক্সপ্লোডার': 'Exploder',
                },
            },
            {
                'id': 'ch4',
                'title': 'আইইডি (IED) - সংজ্ঞা ও প্রকারভেদ',
                'source': 'আইইডি ও সিবিআরএন বই, অধ্যায়-১ থেকে ৪',
                'content': """
## আইইডি (IED) - Improvised Explosive Device

**সংজ্ঞা:** আইইডি হলো অপ্রচলিত কারিগরি জ্ঞান ব্যবহার করে উদ্ভাবিত উপায়ে তৈরি মরণাস্ত্র, যা সন্ত্রাসীরা বিস্ফোরক দ্বারা তৈরি করে এবং নিজেদের ইচ্ছানুযায়ী তা স্থাপন করে।
*(সূত্র: আইইডি ও সিবিআরএন বই)*

আইইডি বিভিন্ন প্রকার হতে পারে:
- ঘড়ি ও সময় দ্বারা নিয়ন্ত্রিত আইইডি
- তার দ্বারা দূরবর্তী অবস্থান হতে নিয়ন্ত্রিত আইইডি
- মোবাইল, রেডিও দ্বারা (তার ব্যতিত) দূরবর্তী অবস্থান হতে নিয়ন্ত্রিত আইইডি
- ক্ষতিগ্রস্থ ব্যক্তি দ্বারা নিজেই সক্রিয়করণ আইইডি
- রকেট বা মর্টার প্রযুক্তি দ্বারা নিয়ন্ত্রিত আইইডি
- মাটির নীচে স্থাপিত, মানুষ বা গাড়ির চাপে সক্রিয় আইইডি

## আইইডির প্রকারভেদ

### ১. অবস্থান ভিত্তিক

| ধরন | পূর্ণ নাম | বর্ণনা |
|-----|-----------|---------|
| **PBIED** | Person Borne IED | ব্যক্তি কর্তৃক বহনকৃত আইইডি (বেল্ট, জ্যাকেট) |
| **VBIED** | Vehicle Borne IED | যানবাহনে বহনকৃত আইইডি (গাড়ি বোম্ব) |
| **SVBIED** | Suicide VBIED | চালক নিজে মারা যায় এমন গাড়ি বোম্ব |
| **RVBIED** | Remote VBIED | দূর থেকে রিমোট কন্ট্রোলে নিয়ন্ত্রিত গাড়ি বোম্ব |
| **UBIED** | Under Body IED | গাড়ির নিচে স্থাপিত আইইডি |

### ২. নিয়ন্ত্রণ ভিত্তিক

| ধরন | পূর্ণ নাম | বর্ণনা |
|-----|-----------|---------|
| **RCIED** | Radio Controlled IED | রেডিও সংকেত দ্বারা নিয়ন্ত্রিত |
| **VOIED/PPIED** | Victim Operated/Pressure Plate IED | ভিকটিমের চাপে সক্রিয় |
| **CWIED** | Command Wire IED | তারের মাধ্যমে নিয়ন্ত্রিত |
| **TIED** | Timed IED | টাইমার দিয়ে নিয়ন্ত্রিত |

### ৩. বিশেষ ধরন

| ধরন | পূর্ণ নাম | বর্ণনা |
|-----|-----------|---------|
| **Suicide IED** | সুইসাইড আইইডি | আত্মঘাতী বিস্ফোরক |
| **Timed IED** | টাইমড আইইডি | ডিজিটাল IC, মাইক্রোপ্রসেসর, রেজিস্টর, ক্যাপাসিটর |
| **VO IED** | Victim Operated IED | ভিকটিম দ্বারা অ্যাকটিভেটেড |
| **Hoax** | হোয়াক্স | দেখতে আইইডির মতো কিন্তু বিস্ফোরণ হয় না |
| **Under-belly IED** | আন্ডারবেলি আইইডি | যানবাহনের নিচে স্থাপিত |

## আইইডির মূল উপাদান

একটি সাধারণ আইইডিতে নিম্নলিখিত উপাদান থাকে:

```
মূল চার্জ (Main Charge)
    ↓
ডেটোনেটর (Detonator)
    ↓
ইনিশিয়েটিং সিস্টেম
    ↓
আর্মিং সুইচ (Arming Switch)
    ↓
ফায়ারিং সুইচ (Firing Switch)
    ↓
পাওয়ার সোর্স (Battery)
```

## হোয়াক্স (Hoax)

কোনো বস্তু বা রিপোর্ট যা দেখতে অবিকল আইইডির মতো এবং কাউন্টার ফোর্সের TTP সম্পর্কে জ্ঞান লাভ করতে সাহায্য করে তাকে হোয়াক্স বলে। হোয়াক্স দ্বারা সেকেন্ডারি ও টার্শিয়ারি অ্যাটাক করে থাকে।
""",
                'key_terms': {
                    'আইইডি': 'IED (Improvised Explosive Device)',
                    'পিবিআইইডি': 'PBIED (Person Borne IED)',
                    'ভিবিআইইডি': 'VBIED (Vehicle Borne IED)',
                    'আরসিআইইডি': 'RCIED (Radio Controlled IED)',
                    'ভিওআইইডি': 'VOIED (Victim Operated IED)',
                    'হোয়াক্স': 'Hoax',
                    'সুইসাইড আইইডি': 'Suicide IED',
                },
            },
            {
                'id': 'ch5',
                'title': 'আইইডির বিভিন্ন সার্কিট ও সুইচ',
                'source': 'আইইডি ও সিবিআরএন বই, অধ্যায়-৫',
                'content': """
## আইইডি সার্কিট

বর্তমান বিশ্বে যে সব আইইডি পাওয়া যাচ্ছে সেই সব আইইডির অধিকাংশেই ইলেকট্রিক সার্কিট ব্যবহৃত হচ্ছে। ইলেকট্রিক সার্কিট ব্যবহারে নিরাপত্তা, নির্ভরযোগ্যতা এবং সহজলভ্যতা সন্ত্রাসীদের নিকট এর ব্যাপক ব্যবহারের কারণ।

### মূল সার্কিট উপাদান

**১. পাওয়ার সোর্স (Battery)**
ব্যাটারি একটি ডিভাইসের জন্য বৈদ্যুতিক শক্তি সরবরাহ করে।

**২. ক্যাপাসিটর**
ক্যাপাসিটর হলো একটি উপাদান যা শক্তি সংরক্ষণ করতে সক্ষম এবং একটি স্থায়ী ভোল্টেজ উৎপন্ন করার মাধ্যমে তার ভোল্টগুলোর মধ্যে চার্জ বা বৈদ্যুতিক শক্তি রূপে সংরক্ষণ করে।

**৩. ট্রানজিস্টর**
ট্রানজিস্টর হল একটি ইলেকট্রনিক উপাদান যা সংকেত বৃদ্ধি করার জন্য ব্যবহৃত হয়। ট্রানজিস্টরের মূলত তিনটি টার্মিনাল থাকে - ইমিটার, কালেক্টর এবং বেস।

**৪. রেজিস্টর**
রেজিস্টর বিদ্যুৎ প্রবাহকে নিয়ন্ত্রণ করে।

### সুইচের প্রকারভেদ

| সুইচ ধরন | ব্যবহার |
|----------|---------|
| **প্রেশার প্লেট সুইচ** | পদচাপে সক্রিয় |
| **টিল্ট সুইচ** | কাত করলে সক্রিয় |
| **পুল সুইচ** | টান দিলে সক্রিয় |
| **টাইমার সুইচ** | নির্দিষ্ট সময়ে সক্রিয় |
| **ফটো সুইচ** | আলোর উপস্থিতিতে সক্রিয় |
| **ম্যাগনেটিক সুইচ** | চুম্বকের সংস্পর্শে সক্রিয় |
| **ভাইব্রেশন সুইচ** | কম্পনে সক্রিয় |

## বেসিক আইইডি সিস্টেম

```
[পাওয়ার সোর্স] → [আর্মিং সুইচ] → [ফায়ারিং সুইচ] → [ডেটোনেটর] → [মেইন চার্জ]
```

## কমান্ড ওয়্যার সিস্টেম

```
[TPU সার্কিট] → [ফায়ারিং ব্যাটারি (১০-৮০০ মিটার দূর)] → [টুইন ফায়ারিং কেবল] → [মেইন চার্জ/মূল বিস্ফোরক] → [ফায়ারিং সুইচ] → [আর্মিং সুইচ]
```
""",
                'key_terms': {
                    'প্রেশার প্লেট': 'Pressure Plate',
                    'টিল্ট সুইচ': 'Tilt Switch',
                    'পুল সুইচ': 'Pull Switch',
                    'ক্যাপাসিটর': 'Capacitor',
                    'ট্রানজিস্টর': 'Transistor',
                },
            },
            {
                'id': 'ch6',
                'title': 'আইইডি নিষ্ক্রিয়করণ পদ্ধতি',
                'source': 'আইইডি ও সিবিআরএন বই, অধ্যায়-২',
                'content': """
## আইইডি ডিসপোজাল (IED Disposal)

সফল আইইডি ডিসপোজাল অপারেশন নিশ্চিত করার জন্য আইইডি ডিসপোজাল দর্শন এবং সাধারণ আইইডি ডিসপোজাল টাস্ক নীতিগুলির প্রয়োগ সম্বন্ধে বোঝা সর্বাধিক গুরুত্বপূর্ণ।

## মূল নীতিসমূহ (Task Reporting Categories)

**প্রথম তদন্ত:** আইইডি হিসেবে শনাক্ত করা বা আইইডি হিসেবে সন্দেহ করা যেত পারে।

### দূরত্ব নির্ধারণ

| আইইডির ধরন | নিরাপদ দূরত্ব |
|-----------|--------------|
| ছোট আইইডি | ৩০০ মিটার |
| মাঝারি আইইডি | ৫০০ মিটার |
| বড় আইইডি/VBIED | ১০০০ মিটার+ |
| SVBIED | ৫০০ মিটার+ |

## EOD প্রবেশ পদ্ধতি

### (১) রিমোট অ্যাপ্রোচ (Remote Approach)
আইইডি ডিসপোজার অপারেটরকে বিপদ এলাকার বাইরে থেকে যতটা সম্ভব করতে হবে। এর মধ্যে দূরবর্তী পর্যবেক্ষণ, প্রয়োজনীয় হিসেবে দৃষ্টি সহায়ক (VISION AIDS) ব্যবহার, ড্রোন এবং হুইল ব্যারোর মতো দূরবর্তী হ্যান্ডলিং সরঞ্জাম ব্যবহার অন্তর্ভুক্ত থাকবে।

### (২) সেমি-রিমোট অ্যাপ্রোচ (Semi Remote Approach)
যদি রিমোট প্রবেশ তত সহজে ব্যবহার না যায়।

### (৩) ম্যানুয়াল অ্যাপ্রোচ (Manual Approach)
সর্বশেষ বিকল্প হিসেবে - EOD অপারেটর নিজে যায়।

## নিষ্ক্রিয়করণ পদ্ধতি

### পদ্ধতি ১: ডিসরাপশন (Disruption)
ডিসরাপ্টর ব্যবহার করে আইইডির পাওয়ার সাপ্লাই বা ফায়ারিং ট্রেন ধ্বংস করা।

### পদ্ধতি ২: নিউট্রালাইজেশন (Neutralization)
ফিউজ বা ট্রিগার মেকানিজম অপসারণ করে আইইডিকে নিরাপদ করা।

### পদ্ধতি ৩: নিয়ন্ত্রিত বিস্ফোরণ (Controlled Detonation)
নিরাপদ স্থানে নিয়ন্ত্রিতভাবে বিস্ফোরণ ঘটানো।

### পদ্ধতি ৪: রেন্ডার সেফ প্রসিডিউর (RSP)
বিশেষজ্ঞ প্রক্রিয়ায় আইইডিকে সম্পূর্ণ নিরাপদ করা।

## EOD সরঞ্জামাদি

| সরঞ্জাম | ব্যবহার |
|---------|---------|
| **রোবট (RORV)** | দূর থেকে আইইডি পরীক্ষা ও নিষ্ক্রিয়করণ |
| **ডিসরাপ্টর** | আইইডির পাওয়ার কাটা |
| **X-Ray মেশিন** | আইইডির ভেতর দেখা |
| **জ্যামার** | রেডিও সংকেত বাধা দেওয়া |
| **EOD স্যুট** | অপারেটরকে সুরক্ষা দেওয়া |
| **ড্রোন** | আকাশ থেকে পর্যবেক্ষণ |
| **ফিউজ এক্সট্র্যাক্টর** | ফিউজ বের করা |
| **নিউট্রালাইজিং কিট** | বিস্ফোরক নিষ্ক্রিয়করণ |
""",
                'key_terms': {
                    'ডিসরাপশন': 'Disruption',
                    'নিউট্রালাইজেশন': 'Neutralization',
                    'নিয়ন্ত্রিত বিস্ফোরণ': 'Controlled Detonation',
                    'রেন্ডার সেফ': 'Render Safe',
                    'EOD': 'Explosive Ordnance Disposal',
                    'রোবট': 'Remote Ordnance Reconnaissance Vehicle (RORV)',
                },
            },
            {
                'id': 'ch7',
                'title': 'সিবিআরএন (CBRN) হুমকি',
                'source': 'আইইডি ও সিবিআরএন বই, সিবিআরএন অধ্যায়',
                'content': """
## সিবিআরএন (CBRN) - Chemical, Biological, Radiological, Nuclear

### পারমাণবিক অস্ত্র (Nuclear Weapons)

যে কোনো অস্ত্রকে দেওয়া একটি সাধারণ নাম যেখানে পারমাণবিক নিউক্লিয়াস, হয় বিদারণ বা ফিউশন বা উভয়ই জড়িত বিক্রিয়ার দ্বারা নির্গত শক্তির ফলে বিস্ফোরণ ঘটে।

**পারমাণবিক বিকিরণ:** বিভিন্ন প্রক্রিয়ার মাধ্যমে পারমাণবিক নিউক্লিয়াস থেকে নির্গত কণা এবং ইলেক্ট্রোম্যাগনেটিক বিকিরণ।

সবচেয়ে গুরুত্বপূর্ণ বিকিরণগুলি হল **আলফা এবং বিটা কণা, গামা রশ্মি এবং নিউট্রন।**

### পারমাণবিক প্রভাব

| প্রভাব | বর্ণনা |
|--------|---------|
| **বিদারণ** | নিউট্রনের বোমাবর্ষণের মাধ্যমে পারমাণবিক নিউক্লিয়াসকে বিভক্ত করার প্রক্রিয়া |
| **দূষণ** | পারমাণবিক বিস্ফোরণের পর তেজস্ক্রিয় পদার্থের জমা |
| **ফলআউট** | বিদারণ পণ্য এবং অন্যান্য ধ্বংসাবশেষ |
| **তাপীয় ডোজ** | পারমাণবিক বিস্ফোরণের পর একটি নির্দিষ্ট এলাকায় (সাধারণত ১ বর্গ সেন্টিমিটার) তাপীয় শক্তি |
| **কিলোটন** | বিস্ফোরণের সময় ১,০০০ টন TNT দ্বারা উৎপাদিত শক্তির সমতুল্য পারমাণবিক অস্ত্রের ফলনের পরিমাপ |
| **মেগাটন** | বিস্ফোরণের সময় ১,০০০,০০০ টন TNT দ্বারা উৎপাদিত শক্তির সমতুল্য |

### রাসায়নিক হুমকি

| শ্রেণি | উদাহরণ | প্রভাব |
|--------|---------|-------|
| **নার্ভ এজেন্ট** | সারিন, ভিএক্স | স্নায়ুতন্ত্র ধ্বংস করে |
| **ব্লিস্টার এজেন্ট** | মাস্টার্ড গ্যাস | ত্বক পোড়ায় |
| **চকিং এজেন্ট** | ক্লোরিন, ফসজিন | শ্বাস বন্ধ করে |
| **রক্ত এজেন্ট** | সায়ানাইড | রক্তে অক্সিজেন বন্ধ করে |

### জৈবিক হুমকি

| প্যাথোজেন | রোগ | বিপদ |
|----------|-----|------|
| **এন্থ্রাক্স** | অ্যান্থ্রাক্স | অত্যন্ত মারাত্মক |
| **প্লেগ** | বুবোনিক প্লেগ | মহামারী সম্ভাবনা |
| **স্মলপক্স** | গুটি বসন্ত | অত্যন্ত সংক্রামক |
| **ইবোলা** | ইবোলা ভাইরাস | উচ্চ মৃত্যুহার |

### সুরক্ষা পদ্ধতি

**MOPP (Mission Oriented Protective Posture) স্তর:**

| স্তর | সুরক্ষা |
|-----|---------|
| MOPP-0 | গিয়ার প্রস্তুত রাখুন |
| MOPP-1 | পোশাক পরুন |
| MOPP-2 | বুট পরুন |
| MOPP-3 | গ্লাভস পরুন |
| MOPP-4 | সম্পূর্ণ গ্যাস মাস্ক ও সুরক্ষা |
""",
                'key_terms': {
                    'সিবিআরএন': 'CBRN (Chemical, Biological, Radiological, Nuclear)',
                    'পারমাণবিক': 'Nuclear',
                    'রাসায়নিক': 'Chemical',
                    'জৈবিক': 'Biological',
                    'রেডিওলজিক্যাল': 'Radiological',
                    'MOPP': 'Mission Oriented Protective Posture',
                    'নার্ভ এজেন্ট': 'Nerve Agent',
                },
            },
            {
                'id': 'ch8',
                'title': 'ল্যান্ড সার্ভিস অ্যামুনিশন ও মাইন',
                'source': 'বিআইডিসি বই-২০২৩',
                'content': """
## ল্যান্ড সার্ভিস অ্যামুনিশন

### গুরুত্বপূর্ণ সংজ্ঞা

**১. অনিষ্পন্ন অর্ডন্যান্স (UXO - Unexploded Ordnance):** বিস্ফোরিত না হওয়া গোলাবারুদ বা বিস্ফোরক বস্তু।

**২. বুলেট:** রাইফেল বা পিস্তল থেকে নিক্ষিপ্ত ধাতব প্রজেক্টাইল।

**৩. প্রজেক্টাইল:** কামান বা মর্টার থেকে নিক্ষিপ্ত বড় ধাতব বস্তু।

**৪. ফিউজ:** গোলার বিস্ফোরণ শুরু করার জন্য ব্যবহৃত ডিভাইস।

### মাইনের প্রকারভেদ

**১. এন্টি-পার্সোনেল মাইন (AP Mine):**
- মানুষকে হত্যা বা আহত করার জন্য
- ভূমিতে অথবা ভূমির কাছাকাছি স্থাপন করা হয়
- পদচাপে বা তারের স্পর্শে বিস্ফোরিত হয়

**২. এন্টি-ট্যাংক মাইন (AT Mine):**
- ট্যাংক বা সাঁজোয়া যান ধ্বংসের জন্য
- বড় চাপে বিস্ফোরিত হয়

**৩. নৌ মাইন (Sea Mine):**
- সমুদ্র বা নদীতে স্থাপিত
- জাহাজ ধ্বংসের জন্য

### সামুদ্রিক মাইনের প্রকারভেদ

| ধরন | বর্ণনা |
|-----|---------|
| **মুড়িং মাইন** | নির্দিষ্ট গভীরতায় স্থির করা |
| **বটম মাইন** | সমুদ্রের তলায় স্থাপিত |
| **ড্রিফটিং মাইন** | ভাসমান মাইন |
| **লিমপেট মাইন** | জাহাজের গায়ে লাগানো |

## মাইনিং অপারেশন নিয়ম

১. মাইনফিল্ডের সীমানা চিহ্নিত করতে হবে
২. মাইনফিল্ডের মানচিত্র রাখতে হবে
৩. মাইন স্থাপনের রেকর্ড রাখতে হবে
৪. মাইনফিল্ডে সতর্কতা চিহ্ন স্থাপন করতে হবে

## মাইন কাউন্টার মেজার্স (MCM)

মাইন পরিষ্কারের জন্য ব্যবহৃত পদ্ধতি:
- **ম্যানুয়াল ডিমাইনিং:** প্রোব ও ডিটেক্টর দিয়ে
- **যান্ত্রিক ডিমাইনিং:** ফ্লেইল বা টিলার মেশিন দিয়ে
- **কুকুর দিয়ে:** প্রশিক্ষিত কুকুর দিয়ে সনাক্তকরণ
""",
                'key_terms': {
                    'UXO': 'Unexploded Ordnance',
                    'AP মাইন': 'Anti-Personnel Mine',
                    'AT মাইন': 'Anti-Tank Mine',
                    'MCM': 'Mine Counter Measures',
                    'মাইনফিল্ড': 'Minefield',
                },
            },
            {
                'id': 'ch9',
                'title': 'EOD সরঞ্জামাদি',
                'source': 'বিআইডিসি বই-২০২৩',
                'content': """
## EOD (Explosive Ordnance Disposal) সরঞ্জাম

বিআইডিসি বই-২০২৩ অনুযায়ী বাংলাদেশ সেনাবাহিনীতে ব্যবহৃত EOD সরঞ্জামাদি:

### রোবটিক সরঞ্জাম

**১. টি-৫ ক্যালিবার রোবট (RORV):**
- দূর থেকে নিয়ন্ত্রিত রোবট
- আইইডি পরীক্ষা ও নিষ্ক্রিয়করণে ব্যবহৃত

**২. ড্রোন:**
- আকাশ থেকে পর্যবেক্ষণ
- সন্দেহজনক এলাকা স্ক্যানিং

### ডিটেকশন সরঞ্জাম

| সরঞ্জাম | উদ্দেশ্য |
|---------|---------|
| **ইউআরসি ১০ কেবল ডিটেক্টর** | তার শনাক্তকরণ |
| **বিডি ইউসি-৫ কেবল ডিটেক্টর** | মাটির নিচের তার |
| **মেটাল ডিটেক্টর** | ধাতব বস্তু |
| **গিগার কাউন্টার** | বিকিরণ পরিমাপ |

### নিষ্ক্রিয়করণ সরঞ্জাম

**১. ডিসরাপ্টর:**
পানির উচ্চ চাপ বা প্রজেক্টাইল দিয়ে আইইডির সার্কিট ধ্বংস করে।

**২. ফিউজ এক্সট্র্যাক্টর:**
আইইডি থেকে ফিউজ বের করার বিশেষ সরঞ্জাম।

**৩. নিউট্রালাইজিং ইকুইপমেন্ট ফিউজ:**
ফিউজকে নিষ্ক্রিয় করার যন্ত্রপাতি।

**৪. ফ্রিজ নিউট্রালাইজিং কিট:**
অতি ঠান্ডায় বিস্ফোরক নিষ্ক্রিয় করার কিট।

**৫. ডি আর্মার কিট:**
বর্ম অপসারণের সরঞ্জাম।

**৬. আর্ডিএস ০৩৯ বোম্ব সাপ্রেশন কন্টেইনার:**
বিস্ফোরক বহন ও পরিবহনের নিরাপদ কন্টেইনার।

### EOD স্যুট

EOD অপারেটরের সুরক্ষার জন্য বিশেষ স্যুট:
- বুলেটপ্রুফ ও ব্লাস্টপ্রুফ আবরণ
- হেলমেট সহ ভিজর
- গ্লাভস
- বুট
- বিশেষ যোগাযোগ সিস্টেম

### জ্যামিং সিস্টেম

**এএলবিপিজি পোর্টেবল জ্যামিং সিস্টেম:**
রেডিও সংকেত জ্যাম করে RCIED প্রতিরোধ করে।
""",
                'key_terms': {
                    'RORV': 'Remote Ordnance Reconnaissance Vehicle',
                    'ডিসরাপ্টর': 'Disruptor',
                    'EOD স্যুট': 'EOD Suit',
                    'জ্যামিং সিস্টেম': 'Jamming System',
                    'ফিউজ এক্সট্র্যাক্টর': 'Fuze Extractor',
                },
            },
            {
                'id': 'ch10',
                'title': 'আইইডি সার্কিট ডায়াগ্রাম',
                'source': 'বিআইডিসি বই-২০২৩, পৃষ্ঠা ১৯২-১৯৬',
                'content': """
## আইইডি সার্কিট ডায়াগ্রাম
*(বিআইডিসি বই-২০২৩ থেকে)*

### ১. কমান্ড ওয়্যার সিস্টেম (COMMAND WIRE SYSTEM)

```
[ফায়ারিং ব্যাটারি] ─── [টুইন ফায়ারিং কেবল (১০-৮০০ মিটার)] ─── [মেইন চার্জ]
```

**বৈশিষ্ট্য:**
- দূরত্ব: ১০ থেকে ৮০০ মিটার
- তার দিয়ে নিয়ন্ত্রিত
- নিশ্চিত ফায়ারিং নিশ্চিত করে

**সনাক্তকরণ:** মাটিতে লুকানো তার, ব্যাটারি সহ বাক্স

---

### ২. টিপিইউ সার্কিট (T.P.U. CIRCUIT)

```
[TIME] ─── [BATTERY]
     └─────── [LAMP]
[DETONATOR] ─── [CLOTHESPEG/MICROSWITCH]
```

**বিশেষ নোট (বই থেকে):**
"LAMP AND CONNECTING WIRE REMOVED WHEN UNIT IS USED IN A VICTIM-OPERATED MODE"
অর্থাৎ ভিকটিম-অপারেটেড মোডে বাতি ও সংযোগকারী তার সরিয়ে দেওয়া হয়।

---

### ৩. বেসিক আরসিআইইডি সিস্টেম (BASIC RCIED SYSTEM)

```
[ট্রান্সমিটার (TX)] ────────────► [রিসিভার (RX)]
                                         │
                                   [ফায়ারিং সুইচ]
                                         │
                                   [মেইন চার্জ]
```

**উপাদান:**
- ট্রান্সমিটার (TX) - দূর থেকে সংকেত পাঠায়
- রিসিভার (RX) - সংকেত গ্রহণ করে
- ফায়ারিং সুইচ
- মেইন চার্জ/প্রধান বিস্ফোরক

---

### ৪. আরসিআইইডি সার্কিট (RCIED CIRCUIT)

```
[RADIO] ─── [BATTERY] ─── [ARMING SWITCH] ─── [FIRING SWITCH] ─── [DETONATOR]
```

**প্রতিরোধ ব্যবস্থা:** ইলেকট্রনিক জ্যামার ব্যবহার করে রেডিও সংকেত বাধা দিন।

---

### ৫. প্রজেক্টাইল কন্ট্রোলড আইইডি (PROJECTILE CONTROLLED IED)

```
[ARMING SWITCH] ─── [BATTERY] ─── [FIRING SWITCH] ─── [DETONATOR]
                              └─── [TWO COPPER PLATES APART WITH SPACERS (APPROX 4'×4')]
```

---

## আইইডি সার্কিটের মূল উপাদান সারসংক্ষেপ

| উপাদান | ভূমিকা |
|--------|--------|
| **ব্যাটারি** | বিদ্যুৎ সরবরাহ |
| **আর্মিং সুইচ** | আইইডিকে সক্রিয় করে |
| **ফায়ারিং সুইচ** | বিস্ফোরণ শুরু করে |
| **ডেটোনেটর** | প্রধান বিস্ফোরক সক্রিয় করে |
| **মেইন চার্জ** | প্রধান বিস্ফোরক |
| **ট্রান্সমিটার/রিসিভার** | দূর থেকে নিয়ন্ত্রণ (RCIED) |
| **টাইমার** | নির্দিষ্ট সময়ে বিস্ফোরণ (TIED) |
| **কপার প্লেট** | প্রেশার সেন্সর হিসেবে |
""",
                'key_terms': {
                    'কমান্ড ওয়্যার': 'Command Wire',
                    'টিপিইউ সার্কিট': 'TPU Circuit',
                    'আরসিআইইডি': 'RCIED (Radio Controlled IED)',
                    'আর্মিং সুইচ': 'Arming Switch',
                    'ফায়ারিং সুইচ': 'Firing Switch',
                    'ট্রান্সমিটার': 'Transmitter (TX)',
                    'রিসিভার': 'Receiver (RX)',
                },
            },
            {
                'id': 'ch11',
                'title': 'ভিবিআইইডি ও সুইসাইড বোম্ব',
                'source': 'বিআইডিসি বই-২০২৩, পৃষ্ঠা ২০৬-২১৩',
                'content': """
## সন্ত্রাসীদের দ্বারা ব্যবহৃত আইইডি সমূহ

বর্তমান বিশ্বে সন্ত্রাসী হামলা প্রতিনিয়ত বৃদ্ধি পাচ্ছে। সন্ত্রাসীরা প্রতিদিন তাদের আক্রমণের পদ্ধতি পরিবর্তন করছে। উদ্ভাবিত এক্সপ্লোসিভ ডিভাইস বা আইইডি সন্ত্রাসীদের সবচেয়ে পছন্দনীয় মাধ্যম।

## ভিবিআইইডি (VBIED - Vehicle Borne IED)

**সংজ্ঞা:** বর্তমানে গাড়ি বোমা একটি অতি পরিচিত শব্দ। বিশ্বে প্রায় প্রতিদিনই বিভিন্ন গাড়ি বোমা বিস্ফোরিত হচ্ছে। গাড়ি বোমা বলতে বোঝায় গাড়িকে আইইডি হিসেবে ব্যবহার করা।

### গাড়িকে আইইডি হিসেবে ব্যবহারের সুবিধা

| সুবিধা | বর্ণনা |
|--------|---------|
| সহজেই পাওয়া যায় | গাড়ি সহজলভ্য |
| আক্রমণ স্থানে গাড়ির অবস্থান | সন্দেহ কম |
| বড় চার্জ বহন সম্ভব | বেশি ক্ষয়ক্ষতি |
| চালক নিজেকে লুকাতে পারে | শনাক্ত করা কঠিন |
| উচ্চ মিডিয়ার দৃষ্টি আকর্ষণ | প্রচার সহজ |

### ভিবিআইইডির প্রকারভেদ

**১. SVBIED (Suicide VBIED):**
চালক নিজে গাড়ি চালিয়ে টার্গেটে ধাক্কা দেয় এবং বিস্ফোরণ ঘটায়।

**২. RVBIED (Remote VBIED):**
দূর থেকে রিমোট কন্ট্রোলের মাধ্যমে গাড়িটি নিয়ন্ত্রণ করা হয়।

**৩. TIED VBIED (Timed):**
টাইমার দিয়ে নির্দিষ্ট সময়ে বিস্ফোরণ ঘটে।

### ভিবিআইইডি শনাক্তকরণ

সন্দেহজনক যানবাহন চেক করার সময় নিম্নলিখিত বিষয়গুলো লক্ষ্য করুন:

- গাড়িটি অস্বাভাবিকভাবে নিচু কি?
- গাড়িতে অস্বাভাবিক কিছু আছে কি?
- চালকের আচরণ সন্দেহজনক কি?
- গাড়িতে অতিরিক্ত ওজন লক্ষণীয় কি?
- গাড়ির লাইসেন্স প্লেট পরিচিত কি?

### RSP (Render Safe Procedure) WARP ব্যবহার

**WARP:** একটি প্রিফেব্রিকেটেড এক্সপ্লোসিভ চার্জ যা চারটি সিলিন্ডার আকারে থাকে এবং সিলিন্ডার চারটি একত্রে সংযুক্ত থাকে। ইহা সাধারণত হুইল ব্যারোর সাহায্যে ব্যবহার করা হয়।

**ব্যবহার প্রক্রিয়া:**
১. গাড়ির গ্লাস খোলা আছে কিনা নিশ্চিত করুন
২. হুইল ব্যারোতে WARP লাগানো থাকে
৩. রিমোটের মাধ্যমে WARP চার্জ ফায়ার করা হয়
৪. নিরাপদ দূরত্ব থেকে অপারেশন পরিচালনা

## উদ্ভাবিত মর্টার (Improvised Mortar)

উদ্ভাবিত মর্টার প্রায় মিলিটারি মর্টারের অনুরূপ তবে এর উপকরণ ভিন্ন। সন্ত্রাসীরা বিভিন্ন রেঞ্জের জন্য বিভিন্ন রকমের কাজের জন্য মর্টার প্রস্তুত করে থাকে।

| ক্যালিবার | ফিলিং | রেঞ্জ |
|----------|-------|-------|
| ছোট ক্যালিবার | ১১.৫ গ্রাম ব্ল্যাক পাউডার | সর্বোচ্চ ১০০ মিটার |
| বড় ক্যালিবার মার্ক-১৫ | ৪০-১২০ কেজি ANS | সর্বোচ্চ ২৭৫ মিটার |
| মার্ক-১৫/১, ১৫/২, ১৫/৩ | ৪০০-৬০০ গ্রাম ব্ল্যাক পাউডার | - |
""",
                'key_terms': {
                    'ভিবিআইইডি': 'VBIED (Vehicle Borne IED)',
                    'এসভিবিআইইডি': 'SVBIED (Suicide VBIED)',
                    'আরভিবিআইইডি': 'RVBIED (Remote VBIED)',
                    'WARP': 'Prefabricated Explosive Charge',
                    'উদ্ভাবিত মর্টার': 'Improvised Mortar',
                    'RSP': 'Render Safe Procedure',
                },
            },
        ]
    },

    'en': {
        'chapters': [
            {
                'id': 'ch1',
                'title': 'Definition and Types of Explosives',
                'source': 'BIDC Book-2023, Chapter-1',
                'content': """
## Explosive

**Definition:** An explosive is a temporary mixture of solid, liquid, or various substances that, in the presence of a necessary initiator, rapidly converts (fully or partially) to permanent gaseous substances generating enormous heat and pressure, destroying objects partially or completely.
*(Source: BIDC Book-2023)*

## Types of Explosives

### 1. Based on Power/Strength

**a) High Explosive:**
High-power explosive, but less sensitive/touch-sensitive than initiating explosive. It explodes when the correct level of detonation wave is applied.

Examples: Hexogen, PE, TNT, etc.

High explosives are of two types:
- **(1) Primary High Explosive:** Initiating Agent - easily detonated
- **(2) Secondary High Explosive:** Bursting Charge - less sensitive, more powerful

**b) Low Explosive:**
Low-power explosive with high touch-sensitivity.

Examples: Gun powder and propellant charge.

### 2. By Use - Three Classes

| Class | Description |
|-------|-------------|
| Initiator | Starts the first explosion |
| Intermediaries | Maintains the connection |
| Bursting Charge | Main explosive charge |

### 3. By Physical Form

- **a) Solid Explosive:** T.N.T (TNT)
- **b) Plastic Explosive:** 808, 851, 852, 2, 3, 3E
- **c) Liquid Explosive:** Nitroglycerine
""",
                'key_terms': {
                    'Explosive': 'বিস্ফোরক',
                    'High Explosive': 'উচ্চ বিস্ফোরক',
                    'Low Explosive': 'নিম্ন বিস্ফোরক',
                    'Detonation': 'ডেটোনেশন',
                    'Initiator': 'ইনিশিয়েটর',
                },
            },
            {
                'id': 'ch2',
                'title': 'Action and Effects of Explosives',
                'source': 'BIDC Book-2023, Chapter-2',
                'content': """
## Action of Explosives

When a high explosive of indeterminate mass and shape detonates, detonation waves spread outward from the center of excitation in a wave pattern. After these shock waves pass, there is the Reaction Zone.

## Effects of Explosives

| Effect | Description |
|--------|-------------|
| **Blast Effect** | Air pressure waves that destroy everything nearby |
| **Fragmentation** | Metal fragments flying at high velocity |
| **Crater Effect** | Formation of a hole in the ground |
| **Thermal Effect** | Fire due to high temperature |
| **Seismic Effect** | Ground vibration |

## Types of Explosions

**1. Mechanical Explosion:** When excessive pressure causes structural failure in a container.

**2. Chemical Explosion:** Explosion resulting from chemical reactions.

**3. Sympathetic Detonation:** When the shock wave from one explosive charge causes detonation of a nearby explosive charge.
""",
                'key_terms': {
                    'Shock Wave': 'শক ওয়েভ',
                    'Blast Effect': 'ব্লাস্ট এফেক্ট',
                    'Fragmentation': 'ফ্র্যাগমেন্টেশন',
                    'Sympathetic Detonation': 'সমবেদী ডেটোনেশন',
                },
            },
            {
                'id': 'ch3',
                'title': 'Demolition Equipment',
                'source': 'BIDC Book-2023, Chapter-3',
                'content': """
## Demolition Equipment

Demolition equipment is generally divided into two categories:

### a) Non-Electric Equipment

1. **Safety Fuze No. 11 Mark-2:** Slow-burning fuze
2. **Safety Fuze Underwater:** Usable underwater
3. **Fuze Instantaneous Mark-4:** Instant ignition
4. **SF Striker:** Activated by friction
5. **SF Friction/Lighter:** Hand-operated lighter
6. **Ignitor Safety Fuze Percussion Mark-3**
7. **Fuzing Match**
8. **Safety Match (Matchsticks)**
9. **Detonator No. 6, 8 and 27**
10. **Primer 1 cm m:**
11. **Detonating Cord**
12. **Primer CE/GC**
13. **Knife and Blade**

### b) Electric Equipment

1. **Exploder Box:** Electrical supply device
2. **Electric Detonator:** Activated by electricity
3. **Ohms Meter Model 205:** Circuit testing instrument
4. **Firing Cable:** Electrical conductor wire

## Use of Detonating Cord

Detonating cord is a plastic-coated cord containing PETN explosive inside. Its burning velocity is 6500 meters per second. Multiple charges can be detonated simultaneously using detonating cord.
""",
                'key_terms': {
                    'Safety Fuze': 'সেফটি ফিউজ',
                    'Detonator': 'ডেটোনেটর',
                    'Detonating Cord': 'ডেটোনেটিং কর্ড',
                    'Ignitor': 'ইগনাইটর',
                    'Exploder': 'এক্সপ্লোডার',
                    'PETN': 'Pentaerythritol Tetranitrate',
                },
            },
            {
                'id': 'ch4',
                'title': 'IED - Definition and Types',
                'source': 'IED & CBRN Book, Chapters 1-4',
                'content': """
## IED - Improvised Explosive Device

**Definition:** An IED is a lethal device made using non-conventional technical knowledge, manufactured by terrorists using explosives, and placed according to their own intent.
*(Source: IED & CBRN Book)*

## Types of IED

### 1. By Location/Carriage

| Type | Full Name | Description |
|------|-----------|-------------|
| **PBIED** | Person Borne IED | Carried by a person (belt, jacket) |
| **VBIED** | Vehicle Borne IED | IED in a vehicle (car bomb) |
| **SVBIED** | Suicide VBIED | Car bomb where driver dies too |
| **RVBIED** | Remote VBIED | Remotely controlled car bomb |
| **UBIED** | Under Body IED | IED placed under a vehicle |

### 2. By Control Method

| Type | Full Name | Description |
|------|-----------|-------------|
| **RCIED** | Radio Controlled IED | Controlled by radio signal |
| **VOIED/PPIED** | Victim Operated/Pressure Plate IED | Activated by victim's pressure |
| **CWIED** | Command Wire IED | Controlled via wire |
| **TIED** | Timed IED | Controlled by timer |

### 3. Special Types

| Type | Full Name | Description |
|------|-----------|-------------|
| **Suicide IED** | Suicide IED | Self-destruct explosive |
| **Timed IED** | Timed IED | Digital IC, microprocessor, resistor, capacitor |
| **VO IED** | Victim Operated IED | Activated by the victim |
| **Hoax** | Hoax | Looks like IED but does not explode |
| **Under-belly IED** | Under-belly IED | Placed under vehicles |

## Key Components of an IED

```
Main Charge (Explosive)
    ↓
Detonator
    ↓
Initiating System
    ↓
Arming Switch
    ↓
Firing Switch
    ↓
Power Source (Battery)
```

## Hoax

Any object or report that looks exactly like an IED and helps adversaries understand counter-force TTP is called a Hoax. Hoax is used for secondary and tertiary attacks.
""",
                'key_terms': {
                    'IED': 'আইইডি (Improvised Explosive Device)',
                    'PBIED': 'পিবিআইইডি (Person Borne IED)',
                    'VBIED': 'ভিবিআইইডি (Vehicle Borne IED)',
                    'RCIED': 'আরসিআইইডি (Radio Controlled IED)',
                    'VOIED': 'ভিওআইইডি (Victim Operated IED)',
                    'Hoax': 'হোয়াক্স',
                },
            },
            {
                'id': 'ch5',
                'title': 'IED Circuits & Switches',
                'source': 'IED & CBRN Book, Chapter-5',
                'content': """
## IED Circuits

Most IEDs found in the world today use electric circuits. Safety, reliability, and ease of availability are the reasons for their widespread use among terrorists.

### Main Circuit Components

**1. Power Source (Battery)**
A battery supplies electrical energy for a device.

**2. Capacitor**
A capacitor is a component capable of storing energy and storing charge or electrical energy between its voltage terminals by producing a steady voltage.

**3. Transistor**
A transistor is an electronic component used to amplify signals. A transistor has three terminals — Emitter, Collector, and Base.

**4. Resistor**
A resistor controls the flow of electricity.

### Types of Switches

| Switch Type | Usage |
|-------------|-------|
| **Pressure Plate Switch** | Activated by foot pressure |
| **Tilt Switch** | Activated when tilted |
| **Pull Switch** | Activated when pulled |
| **Timer Switch** | Activated at a specific time |
| **Photo Switch** | Activated by presence of light |
| **Magnetic Switch** | Activated by contact with magnet |
| **Vibration Switch** | Activated by vibration |

## Basic IED System

```
[Power Source] → [Arming Switch] → [Firing Switch] → [Detonator] → [Main Charge]
```

## Command Wire System

```
[TPU Circuit] → [Firing Battery (10-800 m away)] → [Twin Firing Cable] → [Main Charge] → [Firing Switch] → [Arming Switch]
```
""",
                'key_terms': {
                    'Pressure Plate': 'প্রেশার প্লেট',
                    'Tilt Switch': 'টিল্ট সুইচ',
                    'Pull Switch': 'পুল সুইচ',
                    'Capacitor': 'ক্যাপাসিটর',
                    'Transistor': 'ট্রানজিস্টর',
                    'Arming Switch': 'আর্মিং সুইচ',
                    'Firing Switch': 'ফায়ারিং সুইচ',
                },
            },
            {
                'id': 'ch6',
                'title': 'IED Disposal Methods',
                'source': 'IED & CBRN Book, Chapter-2',
                'content': """
## IED Disposal

Understanding the IED disposal philosophy and application of general IED disposal task principles is most important to ensure successful IED disposal operations.

## Safe Distances

| IED Type | Safe Distance |
|----------|--------------|
| Small IED | 300 meters |
| Medium IED | 500 meters |
| Large IED/VBIED | 1000 meters+ |
| SVBIED | 500 meters+ |

## EOD Approach Methods

### (1) Remote Approach
IED disposal operator must work as much as possible from outside the danger area. This includes remote observation, use of vision aids, drones, and remote handling equipment like wheel barrows.

### (2) Semi-Remote Approach
If remote approach cannot be used as easily.

### (3) Manual Approach
Last resort - EOD operator approaches in person.

## Disposal Methods

### Method 1: Disruption
Using a disruptor to destroy the IED's power supply or firing train.

### Method 2: Neutralization
Removing the fuse or trigger mechanism to make IED safe.

### Method 3: Controlled Detonation
Conducting a controlled detonation in a safe location.

### Method 4: Render Safe Procedure (RSP)
Making the IED completely safe through specialist procedures.

## EOD Equipment

| Equipment | Use |
|-----------|-----|
| **Robot (RORV)** | Remote IED examination and neutralization |
| **Disruptor** | Cut IED power |
| **X-Ray Machine** | See inside IED |
| **Jammer** | Block radio signals |
| **EOD Suit** | Protect operator |
| **Drone** | Aerial observation |
| **Fuze Extractor** | Remove fuze |
| **Neutralizing Kit** | Neutralize explosives |
""",
                'key_terms': {
                    'Disruption': 'ডিসরাপশন',
                    'Neutralization': 'নিউট্রালাইজেশন',
                    'Controlled Detonation': 'নিয়ন্ত্রিত বিস্ফোরণ',
                    'Render Safe': 'রেন্ডার সেফ',
                    'EOD': 'Explosive Ordnance Disposal',
                    'RORV': 'Remote Ordnance Reconnaissance Vehicle',
                },
            },
            {
                'id': 'ch7',
                'title': 'CBRN Threats',
                'source': 'IED & CBRN Book, CBRN Chapters',
                'content': """
## CBRN - Chemical, Biological, Radiological, Nuclear

### Nuclear Weapons

A general name given to any weapon where the explosion occurs due to energy released by reactions involving atomic nuclei, either fission or fusion or both.

**Nuclear Radiation:** Particles and electromagnetic radiation emitted from atomic nuclei through various processes. The most important radiations are **alpha and beta particles, gamma rays, and neutrons.**

### Nuclear Effects

| Effect | Description |
|--------|-------------|
| **Fission** | Process of splitting atomic nucleus through neutron bombardment |
| **Contamination** | Accumulation of radioactive material after nuclear explosion |
| **Fallout** | Fission products and other debris |
| **Thermal Dose** | Thermal energy in a specific area (usually 1 sq cm) |
| **Kiloton** | Equivalent to energy produced by 1,000 tons of TNT |
| **Megaton** | Equivalent to energy produced by 1,000,000 tons of TNT |

### Chemical Threats

| Class | Examples | Effects |
|-------|----------|---------|
| **Nerve Agents** | Sarin, VX | Destroys nervous system |
| **Blister Agents** | Mustard Gas | Burns skin |
| **Choking Agents** | Chlorine, Phosgene | Stops breathing |
| **Blood Agents** | Cyanide | Stops oxygen in blood |

### Biological Threats

| Pathogen | Disease | Danger |
|---------|---------|--------|
| **Anthrax** | Anthrax | Extremely lethal |
| **Plague** | Bubonic Plague | Epidemic potential |
| **Smallpox** | Smallpox | Highly contagious |
| **Ebola** | Ebola Virus | High mortality |

### MOPP Levels

| Level | Protection |
|-------|-----------|
| MOPP-0 | Gear ready |
| MOPP-1 | Wear garment |
| MOPP-2 | Wear boots |
| MOPP-3 | Wear gloves |
| MOPP-4 | Full gas mask and protection |
""",
                'key_terms': {
                    'CBRN': 'সিবিআরএন (Chemical, Biological, Radiological, Nuclear)',
                    'Nuclear': 'পারমাণবিক',
                    'Chemical': 'রাসায়নিক',
                    'Biological': 'জৈবিক',
                    'Radiological': 'রেডিওলজিক্যাল',
                    'MOPP': 'Mission Oriented Protective Posture',
                    'Nerve Agent': 'নার্ভ এজেন্ট',
                },
            },
            {
                'id': 'ch8',
                'title': 'Land Service Ammunition & Mines',
                'source': 'BIDC Book-2023',
                'content': """
## Land Service Ammunition

### Important Definitions

**1. UXO (Unexploded Ordnance):** Ammunition or explosive objects that have not detonated.

**2. Bullet:** A metal projectile fired from a rifle or pistol.

**3. Projectile:** A large metal object fired from a cannon or mortar.

**4. Fuze:** A device used to initiate the explosion of a shell.

### Types of Mines

**1. Anti-Personnel Mine (AP Mine):**
- Designed to kill or injure people
- Placed on or near the ground
- Detonated by footstep pressure or tripwire

**2. Anti-Tank Mine (AT Mine):**
- Designed to destroy tanks or armored vehicles
- Detonated by heavy pressure

**3. Sea Mine:**
- Placed in sea or river
- Designed to destroy ships

### Types of Naval Mines

| Type | Description |
|------|-------------|
| **Mooring Mine** | Fixed at a specific depth |
| **Bottom Mine** | Placed on the seabed |
| **Drifting Mine** | Floating mine |
| **Limpet Mine** | Attached to the hull of a ship |

## Mining Operation Rules

1. Mark the boundaries of the minefield
2. Keep a map of the minefield
3. Keep records of mine placement
4. Place warning signs in minefields

## Mine Counter Measures (MCM)

Methods used for mine clearance:
- **Manual Demining:** Using probe and detector
- **Mechanical Demining:** Using flail or tiller machine
- **Dog Detection:** Detection using trained dogs
""",
                'key_terms': {
                    'UXO': 'Unexploded Ordnance',
                    'AP Mine': 'Anti-Personnel Mine',
                    'AT Mine': 'Anti-Tank Mine',
                    'MCM': 'Mine Counter Measures',
                    'Minefield': 'মাইনফিল্ড',
                    'Fuze': 'ফিউজ',
                },
            },
            {
                'id': 'ch9',
                'title': 'EOD Equipment',
                'source': 'BIDC Book-2023',
                'content': """
## EOD (Explosive Ordnance Disposal) Equipment

EOD equipment used by Bangladesh Army according to BIDC Book-2023:

### Robotic Equipment

**1. T-5 Caliber Robot (RORV):**
- Remotely controlled robot
- Used for IED inspection and neutralization

**2. Drone:**
- Aerial observation
- Scanning of suspicious areas

### Detection Equipment

| Equipment | Purpose |
|-----------|---------|
| **URC 10 Cable Detector** | Wire detection |
| **BD YUC-5 Cable Detector** | Underground wires |
| **Metal Detector** | Metallic objects |
| **Geiger Counter** | Radiation measurement |

### Neutralization Equipment

**1. Disruptor:**
Destroys the IED circuit using high-pressure water or a projectile.

**2. Fuze Extractor:**
Specialist tool for removing the fuze from an IED.

**3. Neutralizing Equipment Fuze:**
Machinery for neutralizing fuzes.

**4. Freeze Neutralizing Kit:**
Kit for neutralizing explosives using extreme cold.

**5. De-Armer Kit:**
Equipment for removing armor.

**6. ARDS 039 Bomb Suppression Container:**
Safe container for carrying and transporting explosives.

### EOD Suit

Special suit for the protection of EOD operators:
- Bulletproof and blast-proof covering
- Helmet with visor
- Gloves
- Boots
- Special communication system

### Jamming System

**ALBPG Portable Jamming System:**
Jams radio signals to prevent RCIED activation.
""",
                'key_terms': {
                    'RORV': 'Remote Ordnance Reconnaissance Vehicle',
                    'Disruptor': 'ডিসরাপ্টর',
                    'EOD Suit': 'ইওডি স্যুট',
                    'Jamming System': 'জ্যামিং সিস্টেম',
                    'Fuze Extractor': 'ফিউজ এক্সট্র্যাক্টর',
                    'Geiger Counter': 'গিগার কাউন্টার',
                },
            },
            {
                'id': 'ch10',
                'title': 'IED Circuit Diagrams',
                'source': 'BIDC Book-2023, Pages 192-196',
                'content': """
## IED Circuit Diagrams
*(From BIDC Book-2023)*

### 1. Command Wire System

```
[Firing Battery] ─── [Twin Firing Cable (10-800 m)] ─── [Main Charge]
```

**Characteristics:**
- Distance: 10 to 800 meters
- Controlled by wire
- Ensures reliable firing

**Detection:** Wire hidden in ground, box with battery

---

### 2. TPU Circuit

```
[TIME] ─── [BATTERY]
     └─────── [LAMP]
[DETONATOR] ─── [CLOTHESPEG/MICROSWITCH]
```

**Special Note (from book):**
"LAMP AND CONNECTING WIRE REMOVED WHEN UNIT IS USED IN A VICTIM-OPERATED MODE"

---

### 3. Basic RCIED System

```
[Transmitter (TX)] ────────────► [Receiver (RX)]
                                       │
                                 [Firing Switch]
                                       │
                                 [Main Charge]
```

**Components:**
- Transmitter (TX) - sends signal from a distance
- Receiver (RX) - receives signal
- Firing Switch
- Main Charge / Main Explosive

---

### 4. RCIED Circuit

```
[RADIO] ─── [BATTERY] ─── [ARMING SWITCH] ─── [FIRING SWITCH] ─── [DETONATOR]
```

**Counter-measure:** Use an electronic jammer to block the radio signal.

---

### 5. Projectile Controlled IED

```
[ARMING SWITCH] ─── [BATTERY] ─── [FIRING SWITCH] ─── [DETONATOR]
                              └─── [TWO COPPER PLATES APART WITH SPACERS (APPROX 4'×4')]
```

---

## IED Circuit Component Summary

| Component | Role |
|-----------|------|
| **Battery** | Supplies electricity |
| **Arming Switch** | Arms the IED |
| **Firing Switch** | Initiates detonation |
| **Detonator** | Activates main charge |
| **Main Charge** | Primary explosive |
| **Transmitter/Receiver** | Remote control (RCIED) |
| **Timer** | Timed detonation (TIED) |
| **Copper Plate** | Acts as pressure sensor |
""",
                'key_terms': {
                    'Command Wire': 'কমান্ড ওয়্যার',
                    'TPU Circuit': 'টিপিইউ সার্কিট',
                    'RCIED': 'Radio Controlled IED',
                    'Arming Switch': 'আর্মিং সুইচ',
                    'Firing Switch': 'ফায়ারিং সুইচ',
                    'Transmitter': 'ট্রান্সমিটার (TX)',
                    'Receiver': 'রিসিভার (RX)',
                },
            },
            {
                'id': 'ch11',
                'title': 'VBIED & Suicide Bomb',
                'source': 'BIDC Book-2023, Pages 206-213',
                'content': """
## IEDs Used by Terrorists

Terrorist attacks are increasing worldwide. Terrorists change their attack methods every day. The Improvised Explosive Device (IED) is the most preferred weapon of terrorists.

## VBIED - Vehicle Borne IED

**Definition:** The car bomb is now a very familiar term. Car bombs detonate somewhere in the world almost every day. Car bomb means using a vehicle as an IED.

### Advantages of Using a Vehicle as an IED

| Advantage | Description |
|-----------|-------------|
| Easily available | Vehicles are accessible |
| Vehicle's presence at target | Less suspicion |
| Can carry large charge | More damage |
| Driver can hide | Difficult to identify |
| High media attention | Easy propaganda |

### Types of VBIED

**1. SVBIED (Suicide VBIED):**
The driver drives the vehicle into the target and detonates the explosion.

**2. RVBIED (Remote VBIED):**
The vehicle is controlled from a distance via remote control.

**3. TIED VBIED (Timed):**
A timer causes detonation at a specific time.

### VBIED Identification

When checking a suspicious vehicle, look for:

- Is the vehicle unusually low?
- Is there anything unusual in the vehicle?
- Is the driver's behavior suspicious?
- Is there visible extra weight in the vehicle?
- Is the vehicle's license plate familiar?

### RSP (Render Safe Procedure) Using WARP

**WARP:** A prefabricated explosive charge that comes in four cylindrical shapes connected together. It is normally used with the help of a wheel barrow.

**Procedure:**
1. Ensure the vehicle's glass is open
2. WARP is fitted to the wheel barrow
3. WARP charge is fired via remote control
4. Operation conducted from safe distance

## Improvised Mortar

The improvised mortar is similar to a military mortar but uses different materials. Terrorists prepare mortars of different types for different ranges.

| Caliber | Filling | Range |
|---------|---------|-------|
| Small Caliber | 11.5 g Black Powder | Max 100 m |
| Large Caliber Mark-15 | 40-120 kg ANS | Max 275 m |
| Mark-15/1, 15/2, 15/3 | 400-600 g Black Powder | — |
""",
                'key_terms': {
                    'VBIED': 'Vehicle Borne IED',
                    'SVBIED': 'Suicide VBIED',
                    'RVBIED': 'Remote VBIED',
                    'WARP': 'Prefabricated Explosive Charge',
                    'Improvised Mortar': 'উদ্ভাবিত মর্টার',
                    'RSP': 'Render Safe Procedure',
                },
            },
        ]
    }
}


def get_knowledge(lang='bn'):
    return BOMB_IED_KNOWLEDGE.get(lang, BOMB_IED_KNOWLEDGE['bn'])


def get_chapter(chapter_id, lang='bn'):
    knowledge = BOMB_IED_KNOWLEDGE.get(lang, BOMB_IED_KNOWLEDGE['bn'])
    for chapter in knowledge.get('chapters', []):
        if chapter['id'] == chapter_id:
            return chapter
    return None
