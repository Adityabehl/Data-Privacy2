# Data Privacy Case Studies

## Aim
To analyze real-world privacy incidents and identify lessons for **prevention** and **response**.

## Case Studies
1. [Equifax Data Breach (2017)](#1-equifax-data-breach-2017)
2. [Cambridge Analytica / Facebook Data Controversy (2018)](#2-cambridge-analytica--facebook-data-controversy-2018)
3. [Marriott (Starwood) Data Breach (2018)](#3-marriott-starwood-data-breach-2018)

---

## 1. Equifax Data Breach (2017)

### What happened?
- In March 2017, a critical vulnerability (**CVE-2017-5638**) was disclosed in Apache Struts, a web application framework, and a patch was released.
- Equifax failed to patch one of its internet-facing dispute portal systems in time.
- Attackers exploited it in **May 2017** and stayed inside the network for about **76 days**, moving laterally and querying databases.
- The breach was discovered on **29 July 2017** and publicly disclosed on **7 September 2017**.
- An expired SSL certificate on a network monitoring tool meant malicious traffic was not being inspected for months.

### What data was involved?
- Roughly **147 million** people (mostly US consumers) affected.
- Full names, **Social Security Numbers**, dates of birth, addresses.
- Driver's licence numbers for some people.
- About **209,000** credit card numbers and ~182,000 dispute documents with personal data.

### Privacy / security impacts
- Very high risk of **identity theft and financial fraud**, since SSNs and birth dates cannot easily be changed.
- Loss of public trust in credit bureaus; executive resignations.
- Settlement with the FTC, CFPB and US states of **up to ~US$700 million**, including consumer compensation and credit monitoring.
- Congressional investigations and tighter scrutiny of credit reporting agencies.

### Controls that could have reduced the risk
| Area | Control |
|---|---|
| Vulnerability management | Timely patching (e.g., within days for critical CVEs); asset inventory so every vulnerable system is known |
| Monitoring | Valid certificates on inspection tools; IDS/IPS and SIEM with alerting |
| Network security | Segmentation to stop lateral movement; web application firewall (WAF) |
| Data protection | Encrypt sensitive data at rest; tokenization of SSNs |
| Access control | Least privilege; rotate credentials; no plaintext credentials on shared drives |
| Governance | Clear patch ownership and accountability; regular penetration testing |

### Lessons for organizations
1. **Patch management is a core security control**, not an IT afterthought.
2. You cannot protect what you do not know you have: maintain an accurate asset inventory.
3. Security tools must be maintained (an expired certificate silently blinded monitoring).
4. Minimise and encrypt highly sensitive identifiers.
5. Prepare a fast, transparent incident response and communication plan.

---

## 2. Cambridge Analytica / Facebook Data Controversy (2018)

### What happened?
- In 2013-14, researcher **Aleksandr Kogan** released the quiz app *"thisisyourdigitallife"* on Facebook.
- About **270,000** people installed it and consented to share data. Under Facebook's platform rules at the time, the app could also collect data of those users' **friends**, who never consented.
- Kogan passed this data to **Cambridge Analytica**, a political consulting firm, in violation of Facebook's platform policy (data was meant for academic use).
- Facebook learned of the misuse in 2015, asked for the data to be deleted and accepted a certification, but did not verify it or notify users.
- Whistleblower Christopher Wylie and journalists exposed the story in **March 2018**.

### What data was involved?
- Profile data of up to **87 million** Facebook users: names, likes, interests, location, friend networks, and in some cases other profile information.
- Data was used to build **psychographic profiles** for political micro-targeting.

### Privacy / security impacts
- Not a hack: this was a **misuse of legitimately accessible data** (a governance and consent failure).
- Users lost control over how their data was reused; people who never used the app were affected.
- Concerns about **manipulation of democratic processes** (US 2016 election, Brexit campaigns).
- Penalties: **US$5 billion FTC settlement** (2019), a US$100 million SEC settlement, a £500,000 UK ICO fine; Cambridge Analytica shut down in 2018.
- Triggered global debate and strengthened enforcement culture around GDPR and similar laws.

### Controls that could have reduced the risk
| Area | Control |
|---|---|
| Consent & transparency | Clear, specific, informed consent; no collection of friends' data without their consent |
| Data minimisation | Restrict third-party API access to only what the app needs |
| Purpose limitation | Technically and contractually enforce "academic use only" |
| Third-party risk management | App review, audits, ongoing monitoring of developers |
| Enforcement | Verify data deletion (audits), not just accept certifications |
| Incident handling | Notify affected users and regulators promptly once misuse is known |
| Governance | Privacy-by-design reviews; strong oversight of platform policies |

### Lessons for organizations
1. **Consent must be meaningful**; one user cannot consent on behalf of their contacts.
2. **Third parties extend your risk**: you stay accountable for data shared through APIs.
3. Policies without technical enforcement and auditing are weak.
4. Respond to known misuse with **verification and disclosure**, not just paperwork.
5. Trust is a business asset; privacy failures carry regulatory and reputational cost.

---

## 3. Marriott (Starwood) Data Breach (2018)

### What happened?
- Marriott acquired Starwood Hotels in **2016**. Attackers had already gained access to the **Starwood guest reservation database in 2014**.
- The intruders stayed undetected for about **four years**, including after the acquisition.
- The breach was discovered in **September 2018** (via an alert from a database security tool) and disclosed on **30 November 2018**.
- Investigators found remote access trojans and credential-harvesting tools, indicating a sophisticated, long-term intrusion.

### What data was involved?
- Initially reported as up to **500 million** guests; later revised to about **383 million** guest records.
- Names, phone numbers, email addresses, mailing addresses, dates of birth, travel details, loyalty account information.
- Millions of **passport numbers** (about 5.25 million unencrypted and 20.3 million encrypted) and several million encrypted payment card numbers.

### Privacy / security impacts
- Risk of identity theft, fraud, phishing, and **targeted surveillance** (passport and travel data are especially sensitive).
- Customer distrust, class-action lawsuits and heavy regulatory attention.
- UK ICO fined Marriott **£18.4 million** under GDPR (reduced from a proposed £99 million); US regulators and state attorneys general also took action.
- Showed that **mergers and acquisitions** can import hidden security debt.

### Controls that could have reduced the risk
| Area | Control |
|---|---|
| M&A due diligence | Full security assessment and remediation of acquired systems before integration |
| Detection | Continuous monitoring, anomaly detection, privileged access monitoring |
| Data protection | Strong encryption with secured key management; restrict storage of passport numbers |
| Access control | MFA, least privilege, regular audit of admin accounts |
| Data minimisation | Delete data no longer needed (retention schedules) |
| Response | Tested incident response plan and prompt notification |

### Lessons for organizations
1. **Inherit risk when you acquire**: do security due diligence on acquired systems.
2. Long dwell time is dangerous; invest in detection, not only prevention.
3. Encrypt sensitive data **and** protect the keys.
4. Collect and retain only what you need.
5. Regulators expect demonstrable accountability under laws like GDPR.

---

## 4. Comparative Summary

| | Equifax | Cambridge Analytica / Facebook | Marriott |
|---|---|---|---|
| Year disclosed | 2017 | 2018 | 2018 |
| Type | External cyberattack | Misuse of data via third party | External cyberattack (long-term) |
| Root cause | Unpatched vulnerability, poor monitoring | Weak consent, weak platform governance and oversight | Inherited compromised system, late detection |
| Affected | ~147 million | Up to ~87 million | ~383 million records |
| Key data | SSN, DOB, address | Profile data, likes, friend networks | Passport, travel, personal details |
| Major penalty | Up to ~US$700M settlement | US$5B FTC; others | £18.4M ICO fine; other actions |
| Core lesson | Patch and monitor | Consent and third-party control | Due diligence and detection |

---

## 5. Overall Lessons

- **Security hygiene matters**: patching, asset inventory, monitoring, encryption.
- **Privacy is more than security**: consent, purpose limitation and data minimisation prevent harm even without a hack.
- **Manage third parties and acquisitions** as part of your own risk surface.
- **Detect faster**: shorter dwell time greatly reduces impact.
- **Respond transparently**: timely notification, support for affected individuals, and cooperation with regulators.
- **Adopt privacy by design and accountability**: regular audits, DPIAs, clear ownership, and board-level oversight.

## Prevention vs. Response Checklist

**Prevention**
- [ ] Maintain asset inventory and patch critical vulnerabilities fast
- [ ] Encrypt sensitive data at rest and in transit
- [ ] Enforce least privilege and MFA
- [ ] Minimise data collection and set retention limits
- [ ] Obtain informed, specific consent
- [ ] Assess third-party vendors and acquisitions

**Detection & Response**
- [ ] Continuous monitoring and logging (SIEM)
- [ ] Documented, tested incident response plan
- [ ] Defined breach notification procedures (regulators and individuals)
- [ ] Post-incident review and corrective actions

## References
- US Senate / House Oversight reports on the Equifax breach; FTC press release on the Equifax settlement (2019)
- UK ICO and FTC documents on Facebook / Cambridge Analytica (2018-2019)
- Marriott International breach disclosure (Nov 2018); UK ICO penalty notice (2020)
