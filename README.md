<!-- ============================================================ -->
<!-- JOB HUNTER AI — Remote Jobs & Internships Board             -->
<!-- Black / Gold / White theme · animated SVG · SEO optimized   -->
<!-- ============================================================ -->

<!-- ===================== HERO BANNER ===================== -->
<p align="center">

<svg width="100%" viewBox="0 0 1000 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="goldText" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFF3C4"/>
      <stop offset="35%" stop-color="#FFD700"/>
      <stop offset="70%" stop-color="#F5A623"/>
      <stop offset="100%" stop-color="#FFE38A"/>
      <animate attributeName="x1" values="0%;100%;0%" dur="8s" repeatCount="indefinite"/>
      <animate attributeName="x2" values="100%;0%;100%" dur="8s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFD700" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="1000" height="300" fill="#050505"/>
  <circle cx="500" cy="150" r="190" fill="url(#glow)"/>

  <!-- floating gold particles -->
  <g>
    <circle cx="120" cy="60" r="3" fill="#FFD700">
      <animate attributeName="cy" values="60;260;60" dur="7s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.2;1" dur="7s" repeatCount="indefinite"/>
    </circle>
    <circle cx="880" cy="240" r="3" fill="#FFD700">
      <animate attributeName="cy" values="240;40;240" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.2;1" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="230" cy="230" r="2.5" fill="#FFE38A">
      <animate attributeName="cy" values="230;60;230" dur="9s" repeatCount="indefinite"/>
    </circle>
    <circle cx="770" cy="80" r="2.5" fill="#FFE38A">
      <animate attributeName="cy" values="80;240;80" dur="8s" repeatCount="indefinite"/>
    </circle>
    <circle cx="60" cy="160" r="2" fill="#F5A623">
      <animate attributeName="cy" values="160;260;160" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="940" cy="140" r="2" fill="#F5A623">
      <animate attributeName="cy" values="140;40;140" dur="5.5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- 3D cube illusion : nested rotating frames -->
  <g transform="translate(180 150)">
    <g>
      <rect x="-55" y="-55" width="110" height="110" fill="none" stroke="#F5A623" stroke-width="2">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="9s" repeatCount="indefinite"/>
      </rect>
      <rect x="-38" y="-38" width="76" height="76" fill="none" stroke="#FFD700" stroke-width="1.5">
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="9s" repeatCount="indefinite"/>
      </rect>
      <rect x="-20" y="-20" width="40" height="40" fill="#FFD700" opacity="0.15">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="9s" repeatCount="indefinite"/>
      </rect>
    </g>
    <ellipse cx="0" cy="0" rx="90" ry="34" fill="none" stroke="#FFD700" stroke-width="1.5" stroke-dasharray="12 10">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="14s" repeatCount="indefinite"/>
    </ellipse>
    <circle cx="90" cy="0" r="4" fill="#FFFFFF">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="14s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- title with animated shine -->
  <g>
    <text x="500" y="128" text-anchor="middle" font-family="Verdana, Arial, sans-serif" font-size="64" font-weight="bold" fill="url(#goldText)" letter-spacing="6">JOB HUNTER AI</text>
    <text x="500" y="128" text-anchor="middle" font-family="Verdana, Arial, sans-serif" font-size="64" font-weight="bold" fill="url(#shine)" letter-spacing="6">
      <animate attributeName="x" values="-400;1400" dur="4.5s" repeatCount="indefinite"/>
    </text>
    <text x="500" y="172" text-anchor="middle" font-family="Verdana, Arial, sans-serif" font-size="20" fill="#FFFFFF" letter-spacing="3">REMOTE JOBS &amp; INTERNSHIPS — UPDATED EVERY 24 HOURS</text>
  </g>

  <!-- 3D stack on right -->
  <g transform="translate(810 150)">
    <g>
      <rect x="-52" y="-52" width="104" height="104" fill="none" stroke="#F5A623" stroke-width="2">
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="11s" repeatCount="indefinite"/>
      </rect>
      <rect x="-34" y="-34" width="68" height="68" fill="none" stroke="#FFD700" stroke-width="1.5">
        <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="11s" repeatCount="indefinite"/>
      </rect>
      <rect x="-16" y="-16" width="32" height="32" fill="#FFD700" opacity="0.2">
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="11s" repeatCount="indefinite"/>
      </rect>
    </g>
    <ellipse cx="0" cy="0" rx="86" ry="30" fill="none" stroke="#F5A623" stroke-width="1.5" stroke-dasharray="10 12">
      <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="12s" repeatCount="indefinite"/>
    </ellipse>
  </g>

  <!-- bottom gold divider with dash flow -->
  <line x1="60" y1="282" x2="940" y2="282" stroke="#FFD700" stroke-width="2" stroke-dasharray="20 14">
    <animate attributeName="stroke-dashoffset" values="0;-136" dur="2.5s" repeatCount="indefinite"/>
  </line>
  <line x1="60" y1="288" x2="940" y2="288" stroke="#F5A623" stroke-width="1" opacity="0.5"/>
</svg>

</p>

<!-- ===================== TYPING ANIMATION ===================== -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=20&duration=3000&pause=900&color=FFD700&background=050505&center=true&vCenter=true&multiline=true&width=820&height=90&lines=100%25+Genuine+Remote+Jobs+%26+Internships;Updated+Every+24+Hours+%E2%80%94+Only+Fresh+Postings;Direct+Apply+Links+from+Real+Company+ATS+Boards;Software+Engineering+%C2%B7+AI+%C2%B7+Cloud+%C2%B7+DevOps+%C2%B7+Design+%C2%B7+Admin+%C2%B7+VA" alt="Job Hunter AI - remote jobs and internships" />
</p>

<!-- ===================== BADGES ===================== -->
<p align="center">
  <a href="https://github.com/aly-abbas11/Job-Hunter-AI/actions/workflows/jobs.yml">
    <img src="https://github.com/aly-abbas11/Job-Hunter-AI/actions/workflows/jobs.yml/badge.svg?branch=main&event=schedule" alt="Job Hunter AI workflow status" />
  </a>
  <a href="https://github.com/aly-abbas11/Job-Hunter-AI/stargazers">
    <img src="https://img.shields.io/github/stars/aly-abbas11/Job-Hunter-AI?style=for-the-badge&label=STARS&labelColor=0A0A0A&color=FFD700" alt="GitHub stars" />
  </a>
  <a href="https://github.com/aly-abbas11/Job-Hunter-AI/network">
    <img src="https://img.shields.io/github/forks/aly-abbas11/Job-Hunter-AI?style=for-the-badge&label=FORKS&labelColor=0A0A0A&color=F5A623" alt="GitHub forks" />
  </a>
  <a href="https://github.com/aly-abbas11/Job-Hunter-AI/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-FFD700?style=for-the-badge&labelColor=0A0A0A&color=FFD700" alt="MIT license" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.12-FFD700?style=for-the-badge&logo=python&logoColor=FFD700&labelColor=0A0A0A&color=F5A623" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/Automated-GitHub%20Actions-FFD700?style=for-the-badge&labelColor=0A0A0A&color=FFD700" alt="GitHub Actions automation" />
  <a href="https://api.visitorbadge.io/api/visitors?path=aly-abbas11%2FJob-Hunter-AI&label=VISITORS&labelColor=0A0A0A&countColor=FFD700">
    <img src="https://api.visitorbadge.io/api/visitors?path=aly-abbas11%2FJob-Hunter-AI&label=VISITORS&labelColor=0A0A0A&countColor=FFD700&style=flat" alt="Repo visitors counter" />
  </a>
</p>

<!-- ===================== ABOUT ===================== -->
## About — Remote Jobs & Internships, Fresh Every 24 Hours

**Job Hunter AI** is an automated **remote jobs board** that collects **genuine remote work opportunities** — software engineering, AI, machine learning, cloud, DevOps, QA, cybersecurity, data, virtual assistant, admin, graphics design, and writing roles — directly from **company applicant tracking systems (Greenhouse, Ashby)** and curated remote-first job boards (RemoteOK, Arbeitnow, Remotive).

Unlike generic job search sites, **every single posting is 100% remote**, no hybrid bait-and-switch. Only jobs and internships posted in the **last 24 hours** are shown, so you always see fresh opportunities before they get 300+ applications. Every listing links **directly to the official apply page** — no middleman, no account required, no dead-end CV submissions.

> **100% remote · 24-hour freshness · direct apply links · ATS-sourced · scam-filtered**

<!-- ===================== LIVE STATISTICS ===================== -->
## Live Board Statistics

<table>
  <tr>
    <td style="background-color:#0A0A0A;border:2px solid #FFD700;text-align:center;padding:10px 22px;">
      <strong style="color:#FFD700;font-size:22px;">28</strong><br/>
      <span style="color:#FFFFFF;">Remote Jobs &amp; Internships</span>
    </td>
    <td style="background-color:#0A0A0A;border:2px solid #F5A623;text-align:center;padding:10px 22px;">
      <strong style="color:#FFD700;font-size:22px;">11</strong><br/>
      <span style="color:#FFFFFF;">New This Run</span>
    </td>
    <td style="background-color:#0A0A0A;border:2px solid #FFD700;text-align:center;padding:10px 22px;">
      <strong style="color:#FFD700;font-size:22px;">25</strong><br/>
      <span style="color:#FFFFFF;">Remote Positions</span>
    </td>
    <td style="background-color:#0A0A0A;border:2px solid #F5A623;text-align:center;padding:10px 22px;">
      <strong style="color:#FFD700;font-size:22px;">1</strong><br/>
      <span style="color:#FFFFFF;">Internships</span>
    </td>
    <td style="background-color:#0A0A0A;border:2px solid #FFD700;text-align:center;padding:10px 22px;">
      <strong style="color:#FFD700;font-size:22px;">4</strong><br/>
      <span style="color:#FFFFFF;">Career Starter Roles</span>
    </td>
  </tr>
</table>

<p align="center" style="color:#8a8a8a;font-size:13px;">
  Last updated <strong style="color:#FFD700;">12 August 2026 13:02 UTC</strong> · Jobs removed since last run: <strong style="color:#FFFFFF;">6</strong>
</p>

<!-- ===================== TECH JOBS ===================== -->
## Latest Remote Software Engineering & Tech Jobs

<table align="center" style="border-collapse:collapse;max-width:980px;width:100%;">
  <tr>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Company</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Position</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Location</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Source</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Apply</th>
  </tr><tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">OpenAI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Backend Software Engineer - Codex for Finance</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/openai/a23bd45a-e192-460d-bd34-a0f6c4bc6865" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">OpenAI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Order Management &amp; Billing Lead — Cloud Marketplaces &amp; Partnerships</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/openai/1e28e1f0-2580-46d9-b5ba-55c77d706f81" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">OpenAI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Manager, Order to Cash — AI Products &amp; Cloud Partnerships</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/openai/103d7043-28ec-4639-9c8d-0910083a1755" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">GitLab</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Software Engineer (Typescript), AI Clients: Duo CLI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote, Poland; Remote, United Kingdom</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://job-boards.greenhouse.io/gitlab/jobs/8693103002" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Instacart</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Manager, Legal Technology, Operations &amp; AI Enablement</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Canada - Remote (ON, AB, BC, or NS Only)</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://instacart.careers/job/?gh_jid=8122333" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Instacart</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Manager, Legal Technology, Operations &amp; AI Enablement</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">United States - Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://instacart.careers/job/?gh_jid=8122176" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">OpenAI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Enterprise Sales Manager, Energy</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/openai/43015fcc-fa12-4842-83d2-f9ae9376c550" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">OpenAI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Technical Program Manager, AI Safety &amp; Safeguards</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/openai/60b966d1-9c7f-4f61-b05e-7bda3e0b0a69" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">OpenAI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Actuator Design Engineer</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/openai/5b75027a-a5eb-4d28-a608-aa6bebcb079f" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">GitLab</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Fullstack Engineer, Marketing</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote, United Kingdom</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://job-boards.greenhouse.io/gitlab/jobs/8697493002" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Seitenbau Gmbh</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">DevOps &amp; Cloud Engineer (m/w/d) - Konstanz, Berlin oder remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.co.uk/jobs/companies/seitenbau-gmbh/devops-cloud-engineer-konstanz-berlin-oder-remote-104284" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">GitLab</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Backend Engineer (Ruby), Plan: Spec-Driven Development</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote, Poland; Remote, United Kingdom</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://job-boards.greenhouse.io/gitlab/jobs/8682860002" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Ramp</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Technical Consultant, Enterprise, Oracle Cloud</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/ramp/6a3f42e6-00d6-4e9d-9caa-9663ffac6d53" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">GrowInTheRole</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Technical Product Manager:in AI &amp; Operations (m/w/d) in einem KI-Start-up</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Köln</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.com/jobs/companies/growintherole/technical-product-managerin-ai-operations-in-einem-ki-start-up-koln-432369" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Soda Data Nv</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Full-Stack Engineer (Backend + Frontend)</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Germany</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.com/jobs/companies/soda-data-nv/remote-senior-full-stack-engineer-backend-frontend-germany-88363" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Metanoia IT Solutions GmbH</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Fullstack Developer (m/w/d)</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Hamburg</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.com/jobs/companies/metanoia-it-solutions-gmbh/fullstack-developer-hamburg-361101" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Seitenbau Gmbh</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Site Reliability Engineer (m/w/d) – Konstanz, Berlin oder remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.co.uk/jobs/companies/seitenbau-gmbh/site-reliability-engineer-konstanz-berlin-oder-remote-382272" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Seitenbau Gmbh</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Java Developer (m/w/d) - Konstanz, Berlin oder remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.co.uk/jobs/companies/seitenbau-gmbh/senior-java-developer-konstanz-berlin-oder-remote-146101" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Coinbase</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Engineering Manager, Core Automation (Platform)</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote - USA</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.coinbase.com/careers/positions/8124224?gh_jid=8124224" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">GitLab</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Principal Program Manager, Go-To-Market</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote, Canada; Remote, United States</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://job-boards.greenhouse.io/gitlab/jobs/8697215002" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Reddit</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Staff Machine Learning Engineer, Feed Relevance</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote - United States</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://job-boards.greenhouse.io/reddit/jobs/8122606" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Ramp</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Data Scientist, Finance</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/ramp/aa5512b1-d973-4d74-9d10-d56446ecf803" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Soda Data Nv</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Frontend Engineer (Full-stack)</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Germany</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.com/jobs/companies/soda-data-nv/remote-senior-frontend-engineer-full-stack-germany-21527" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Soda Data Nv</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Senior Backend + Infrastructure Engineer (Platform)</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Germany</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.com/jobs/companies/soda-data-nv/remote-senior-backend-infrastructure-engineer-platform-germany-169316" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
</table>

<!-- ===================== STARTER JOBS ===================== -->
## Career Starter Opportunities — No Experience Needed

> Admin, virtual assistant, graphics & design, writing, and customer support roles — perfect for juniors, students, and career switchers looking for **entry level remote jobs**.

<table align="center" style="border-collapse:collapse;max-width:980px;width:100%;">
  <tr>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Company</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Position</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Location</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Source</th>
    <th style="background-color:#FFD700;border:1px solid #FFD700;padding:8px 12px;color:#050505;">Apply</th>
  </tr><tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">OpenAI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Product Designer, GenUI</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/openai/7c1cd1ec-47a9-4d15-8eb9-2f44272db796" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Reddit</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Principal UX Engineer, Ads</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote - United States</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Greenhouse</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://job-boards.greenhouse.io/reddit/jobs/8122887" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Ramp</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Associate Manager, Premier Support (Customer Experience)</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Remote</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Ashby</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://jobs.ashbyhq.com/ramp/2ddd97a8-70b2-4030-ba42-21124ad304d3" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
<tr>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFFFFF;">Nutrition-Plus Germany e.K.</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#FFD700;">Social Media Manager (m/w/d) - Schwerpunkt TikTok Content - Vollzeit, 100 % Homeoffice</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#D9D9D9;">Grafschaft</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;color:#F5A623;">Arbeitnow</td>
      <td style="background-color:#0A0A0A;border:1px solid #2A2A2A;padding:8px 12px;text-align:center;"><a href="https://www.arbeitnow.com/jobs/companies/nutrition-plus-germany-ek/social-media-manager-schwerpunkt-tiktok-content-vollzeit-100-homeoffice-grafschaft-308402" style="color:#050505;background-color:#FFD700;text-decoration:none;font-weight:bold;padding:4px 14px;border-radius:4px;">APPLY</a></td>
    </tr>
</table>

<!-- ===================== ANIMATED DIVIDER ===================== -->
<p align="center">
<svg width="100%" viewBox="0 0 1000 40" xmlns="http://www.w3.org/2000/svg">
  <rect width="1000" height="40" fill="#050505"/>
  <line x1="40" y1="20" x2="960" y2="20" stroke="#FFD700" stroke-width="2" stroke-dasharray="30 16">
    <animate attributeName="stroke-dashoffset" values="0;-184" dur="3s" repeatCount="indefinite"/>
  </line>
  <circle cx="500" cy="20" r="6" fill="#FFD700">
    <animate attributeName="r" values="6;9;6" dur="1.8s" repeatCount="indefinite"/>
  </circle>
  <circle cx="500" cy="20" r="10" fill="none" stroke="#F5A623" stroke-width="1.5" opacity="0.6">
    <animate attributeName="r" values="10;18;10" dur="1.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0;0.6" dur="1.8s" repeatCount="indefinite"/>
  </circle>
</svg>
</p>

<!-- ===================== SOURCES ===================== -->
## Sources — Where These Remote Jobs Come From

Jobs are fetched from **five trusted platforms** and filtered for quality:

| Source | Type | Why It's Trusted |
|---|---|---|
| **Greenhouse** | Company ATS | Airbnb, Stripe, GitLab, Reddit, Pinterest, Cloudflare, Coinbase, Roblox, Dropbox, Instacart, Datadog — jobs often **not posted anywhere else** |
| **Ashby** | Company ATS | OpenAI, Ramp, Linear, Supabase, Resend, Warp |
| **Remotive** | Curated board | Human-reviewed remote jobs with an active community |
| **Arbeitnow** | Remote-first board | EU remote opportunities with direct apply pages |

<!-- ===================== WHY GENUINE ===================== -->
## Why These Are Genuine Jobs — Not CV Black Holes

- **ATS-sourced**: Greenhouse and Ashby listings are official company career pages — you apply straight into the employer's own hiring system, which converts **~3-6x better** than mass job board applications.
- **Curated boards only**: Remotive manually reviews listings, and RemoteOK's paid posting model keeps out scam postings.
- **24-hour freshness**: Listings older than 24 hours are automatically dropped. Fresh remote jobs get up to **80% fewer applications** — your best chance of being seen.
- **Scam filter**: Data entry, transcription, and "make money online" listings are deliberately excluded — the top scam categories per FTC guidance.
- **100% remote only**: No hybrid bait. Every job passes an automatic remote check.

<!-- ===================== FEATURES ===================== -->
## Features

- Automated remote jobs & internships aggregation — no manual checking of 10 sites
- Smart filtering: tech, AI, Python, Java, cloud, DevOps, QA, security, data, design, admin, VA
- Duplicate detection and job scoring
- Snapshot diffing — see what's new and what's gone every run
- Automatic README generation with direct apply links
- GitHub Actions automation (scheduled + manual dispatch)
- Fully unit tested (30+ tests)

## Tech Stack

Python · GitHub Actions · REST APIs · RSS · Automation · Open Source

<!-- ===================== KEYWORDS ===================== -->
## Search Keywords

**remote jobs** · **work from home jobs** · **remote internships** · **software engineering jobs** · **junior developer jobs** · **entry level remote jobs** · **virtual assistant jobs** · **graphic design jobs remote** · **remote AI jobs** · **machine learning jobs remote** · **cloud engineer jobs remote** · **DevOps jobs remote** · **QA jobs remote** · **data analyst jobs remote** · **remote-first companies** · **fully remote work** · **jobs hiring immediately** · **apply direct no portal**

<!-- ===================== CONTRIBUTING ===================== -->
## Contributing

Found a great remote job source or want to add more companies? Contributions are welcome — open an issue or a pull request.

**Star this repository** to keep the board alive and growing.

---

<p align="center">
  <span style="color:#8a8a8a;">Job Hunter AI — your automated gateway to</span>
  <strong style="color:#FFD700;">genuine remote jobs &amp; internships</strong>
  <br/>
  <a href="https://github.com/aly-abbas11/Job-Hunter-AI">
    <img src="https://img.shields.io/badge/GitHub-aly--abbas11%2FJob--Hunter--AI-FFD700?style=flat-square&labelColor=0A0A0A&color=FFD700" alt="GitHub repository" />
  </a>
  <img src="https://api.visitorbadge.io/api/visitors?path=aly-abbas11%2FJob-Hunter-AI&label=VISITORS&labelColor=0A0A0A&countColor=FFD700&style=flat" alt="Visitor counter" />
</p>

<p align="center">
<svg width="100%" viewBox="0 0 1000 30" xmlns="http://www.w3.org/2000/svg">
  <rect width="1000" height="30" fill="#050505"/>
  <line x1="100" y1="15" x2="900" y2="15" stroke="#F5A623" stroke-width="1.5" stroke-dasharray="16 12">
    <animate attributeName="stroke-dashoffset" values="0;-112" dur="2s" repeatCount="indefinite"/>
  </line>
</svg>
</p>
