<svg class="ai-diagram" viewBox="0 0 500 440" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="velGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" style="stop-color:#06B6D4;stop-opacity:1"/>
              <stop offset="100%" style="stop-color:#0EA5E9;stop-opacity:1"/>
            </linearGradient>
            <radialGradient id="velGlow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" style="stop-color:#06B6D4;stop-opacity:0.28"/>
              <stop offset="100%" style="stop-color:#06B6D4;stop-opacity:0"/>
            </radialGradient>
          </defs>

          <!-- ── VELOCITY BADGE (top centre) ── -->
          <circle cx="250" cy="108" r="82" fill="url(#velGlow)">
            <animate attributeName="r" values="80;94;80" dur="3s" repeatCount="indefinite"/>
          </circle>
          <circle cx="250" cy="108" r="70" fill="#0A1628" stroke="#06B6D4" stroke-width="2"/>
          <circle cx="250" cy="108" r="62" fill="none" stroke="rgba(6,182,212,0.18)" stroke-width="1"/>
          <text x="250" y="96" text-anchor="middle" fill="#06B6D4" font-size="40" font-weight="700" font-family="Space Grotesk, sans-serif">2&#8288;&#8209;&#8288;3&#xD7;</text>
          <text x="250" y="116" text-anchor="middle" fill="rgba(255,255,255,0.75)" font-size="11" font-weight="600" font-family="Space Grotesk, sans-serif">FASTER</text>
          <text x="250" y="132" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="9" font-family="Space Grotesk, sans-serif">DELIVERY</text>

          <!-- Sub-label -->
          <text x="250" y="204" text-anchor="middle" fill="rgba(255,255,255,0.38)" font-size="8.5" font-weight="700" letter-spacing="0.1em" font-family="Space Grotesk, sans-serif">HOW WE DELIVER YOUR PROJECT</text>

          <!-- ── MILESTONE TRACK ── -->
          <!-- Track background -->
          <line x1="42" y1="242" x2="458" y2="242" stroke="#1E293B" stroke-width="3" stroke-linecap="round"/>
          <!-- Animated progress fill (length = 416) -->
          <line x1="42" y1="242" x2="458" y2="242" stroke="url(#velGrad)" stroke-width="3" stroke-linecap="round" stroke-dasharray="416" stroke-dashoffset="416">
            <animate attributeName="stroke-dashoffset" values="416;312;208;104;0;0;416" keyTimes="0;0.2;0.4;0.6;0.78;0.9;1" dur="7s" repeatCount="indefinite"/>
          </line>

          <!-- Milestone 1: PLAN (x=42) — starts lit -->
          <circle cx="42" cy="242" r="19" fill="#06B6D4" stroke="#06B6D4" stroke-width="2">
            <animate attributeName="fill" calcMode="discrete" values="#06B6D4;#06B6D4;#06B6D4;#06B6D4;#06B6D4;#06B6D4;#0A1628" keyTimes="0;0.2;0.4;0.6;0.78;0.9;1" dur="7s" repeatCount="indefinite"/>
          </circle>
          <text x="42" y="247" text-anchor="middle" fill="white" font-size="9" font-weight="700" font-family="Space Grotesk, sans-serif">P</text>
          <text x="42" y="272" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="8.5" font-family="Space Grotesk, sans-serif">PLAN</text>

          <!-- Milestone 2: DESIGN (x=146) -->
          <circle cx="146" cy="242" r="19" fill="#0A1628" stroke="#06B6D4" stroke-width="2">
            <animate attributeName="fill" calcMode="discrete" values="#0A1628;#06B6D4;#06B6D4;#06B6D4;#06B6D4;#06B6D4;#0A1628" keyTimes="0;0.2;0.4;0.6;0.78;0.9;1" dur="7s" repeatCount="indefinite"/>
          </circle>
          <text x="146" y="247" text-anchor="middle" fill="white" font-size="9" font-weight="700" font-family="Space Grotesk, sans-serif">D</text>
          <text x="146" y="272" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="8.5" font-family="Space Grotesk, sans-serif">DESIGN</text>

          <!-- Milestone 3: BUILD (x=250) -->
          <circle cx="250" cy="242" r="19" fill="#0A1628" stroke="#06B6D4" stroke-width="2">
            <animate attributeName="fill" calcMode="discrete" values="#0A1628;#0A1628;#06B6D4;#06B6D4;#06B6D4;#06B6D4;#0A1628" keyTimes="0;0.2;0.4;0.6;0.78;0.9;1" dur="7s" repeatCount="indefinite"/>
          </circle>
          <text x="250" y="247" text-anchor="middle" fill="white" font-size="9" font-weight="700" font-family="Space Grotesk, sans-serif">B</text>
          <text x="250" y="272" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="8.5" font-family="Space Grotesk, sans-serif">BUILD</text>
          <!-- AI spark badge on BUILD -->
          <circle cx="268" cy="226" r="9" fill="#0EA5E9"/>
          <text x="268" y="230" text-anchor="middle" fill="white" font-size="8" font-weight="700" font-family="Space Grotesk, sans-serif">AI</text>

          <!-- Milestone 4: TEST (x=354) -->
          <circle cx="354" cy="242" r="19" fill="#0A1628" stroke="#06B6D4" stroke-width="2">
            <animate attributeName="fill" calcMode="discrete" values="#0A1628;#0A1628;#0A1628;#06B6D4;#06B6D4;#06B6D4;#0A1628" keyTimes="0;0.2;0.4;0.6;0.78;0.9;1" dur="7s" repeatCount="indefinite"/>
          </circle>
          <text x="354" y="247" text-anchor="middle" fill="white" font-size="9" font-weight="700" font-family="Space Grotesk, sans-serif">T</text>
          <text x="354" y="272" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="8.5" font-family="Space Grotesk, sans-serif">TEST</text>

          <!-- Milestone 5: SHIP (x=458) -->
          <circle cx="458" cy="242" r="19" fill="#0A1628" stroke="#06B6D4" stroke-width="2">
            <animate attributeName="fill" calcMode="discrete" values="#0A1628;#0A1628;#0A1628;#0A1628;#06B6D4;#06B6D4;#0A1628" keyTimes="0;0.2;0.4;0.6;0.78;0.9;1" dur="7s" repeatCount="indefinite"/>
          </circle>
          <text x="458" y="247" text-anchor="middle" fill="white" font-size="9" font-weight="700" font-family="Space Grotesk, sans-serif">S</text>
          <text x="458" y="272" text-anchor="middle" fill="rgba(255,255,255,0.55)" font-size="8.5" font-family="Space Grotesk, sans-serif">SHIP</text>

          <!-- Travelling dot -->
          <circle cx="42" cy="242" r="6" fill="white" opacity="0.9">
            <animate attributeName="cx" calcMode="linear" values="42;146;250;354;458;458;42" keyTimes="0;0.2;0.4;0.6;0.78;0.9;1" dur="7s" repeatCount="indefinite"/>
            <animate attributeName="opacity" calcMode="discrete" values="0.9;0.9;0.9;0.9;0.9;0;0" keyTimes="0;0.2;0.4;0.6;0.78;0.9;1" dur="7s" repeatCount="indefinite"/>
          </circle>

          <!-- ── TIMELINE COMPARISON ── -->
          <text x="250" y="313" text-anchor="middle" fill="rgba(255,255,255,0.35)" font-size="8" font-weight="700" letter-spacing="0.09em" font-family="Space Grotesk, sans-serif">PROJECT TIMELINE COMPARISON</text>

          <!-- Traditional bar -->
          <text x="36" y="340" fill="rgba(255,255,255,0.5)" font-size="9" font-family="Space Grotesk, sans-serif">Traditional</text>
          <rect x="120" y="328" width="310" height="17" rx="4" fill="#1E293B"/>
          <rect x="120" y="328" width="310" height="17" rx="4" fill="#334155"/>
          <text x="436" y="340" fill="rgba(255,255,255,0.45)" font-size="9" font-family="Space Grotesk, sans-serif">12 mo.</text>

          <!-- CloudZoom bar -->
          <text x="36" y="368" fill="rgba(255,255,255,0.5)" font-size="9" font-family="Space Grotesk, sans-serif">CloudZoom</text>
          <rect x="120" y="356" width="310" height="17" rx="4" fill="#1E293B"/>
          <!-- Animated fill -->
          <rect x="120" y="356" width="0" height="17" rx="4" fill="url(#velGrad)">
            <animate attributeName="width" values="0;0;114;114;0" keyTimes="0;0.05;0.5;0.9;1" dur="7s" repeatCount="indefinite"/>
          </rect>
          <!-- "4 mo." label fades in with bar -->
          <text x="240" y="368" fill="#06B6D4" font-size="9" font-weight="600" font-family="Space Grotesk, sans-serif" opacity="0">4 mo.
            <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;0.45;0.5;0.9;1" dur="7s" repeatCount="indefinite"/>
          </text>

          <!-- Savings badge -->
          <rect x="342" y="348" width="96" height="26" rx="5" fill="rgba(6,182,212,0.12)" stroke="#06B6D4" stroke-width="1"/>
          <text x="390" y="365" text-anchor="middle" fill="#06B6D4" font-size="10" font-weight="700" font-family="Space Grotesk, sans-serif">2&#8288;&#8209;&#8288;3&#xD7; faster</text>

          <!-- Footer note -->
          <text x="250" y="422" text-anchor="middle" fill="rgba(255,255,255,0.28)" font-size="9" font-family="Space Grotesk, sans-serif">AI-assisted tools cut build time &#8212; savings passed directly to you</text>
        </svg>