<svg viewBox="0 0 420 210" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
          <text x="210" y="22" text-anchor="middle" fill="rgba(255,255,255,0.45)" font-size="8.5" font-weight="700" letter-spacing="0.1em" font-family="Space Grotesk, sans-serif">AI WORKFLOW PIPELINE</text>

          <!-- Stage boxes -->
          <!-- Stage 1: REQUEST -->
          <rect x="8" y="38" width="68" height="52" rx="8" fill="#0D2545" stroke="#06B6D4" stroke-width="1.5"><animate attributeName="fill" values="#06B6D4;#06B6D4;#06B6D4;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#06B6D4" keyTimes="0;0.05;0.22;0.27;0.44;0.49;0.66;0.71;0.88;0.93;1" dur="5s" repeatCount="indefinite"/></rect>
          <text x="42" y="59" text-anchor="middle" fill="white" font-size="8" font-weight="700" font-family="Space Grotesk, sans-serif">REQUEST</text>
          <text x="42" y="73" text-anchor="middle" fill="rgba(255,255,255,0.65)" font-size="7.5" font-family="Space Grotesk, sans-serif">Inbound</text>

          <!-- Arrow 1 -->
          <line x1="78" y1="64" x2="88" y2="64" stroke="#06B6D4" stroke-width="1.5" opacity="0.6"/>
          <polygon points="86,59 96,64 86,69" fill="#06B6D4" opacity="0.7"/>

          <!-- Stage 2: RECEIVE -->
          <rect x="98" y="38" width="68" height="52" rx="8" fill="#0D2545" stroke="#06B6D4" stroke-width="1.5"><animate attributeName="fill" values="#0D2545;#0D2545;#0D2545;#06B6D4;#06B6D4;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545" keyTimes="0;0.05;0.22;0.27;0.44;0.49;0.66;0.71;0.88;0.93;1" dur="5s" repeatCount="indefinite"/></rect>
          <text x="132" y="59" text-anchor="middle" fill="white" font-size="8" font-weight="700" font-family="Space Grotesk, sans-serif">RECEIVE</text>
          <text x="132" y="73" text-anchor="middle" fill="rgba(255,255,255,0.65)" font-size="7.5" font-family="Space Grotesk, sans-serif">AI picks up</text>

          <!-- Arrow 2 -->
          <line x1="168" y1="64" x2="178" y2="64" stroke="#06B6D4" stroke-width="1.5" opacity="0.6"/>
          <polygon points="176,59 186,64 176,69" fill="#06B6D4" opacity="0.7"/>

          <!-- Stage 3: QUALIFY -->
          <rect x="188" y="38" width="68" height="52" rx="8" fill="#0D2545" stroke="#06B6D4" stroke-width="1.5"><animate attributeName="fill" values="#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#06B6D4;#06B6D4;#0D2545;#0D2545;#0D2545;#0D2545" keyTimes="0;0.05;0.22;0.27;0.44;0.49;0.66;0.71;0.88;0.93;1" dur="5s" repeatCount="indefinite"/></rect>
          <text x="222" y="59" text-anchor="middle" fill="white" font-size="8" font-weight="700" font-family="Space Grotesk, sans-serif">QUALIFY</text>
          <text x="222" y="73" text-anchor="middle" fill="rgba(255,255,255,0.65)" font-size="7.5" font-family="Space Grotesk, sans-serif">&amp; Route</text>

          <!-- Arrow 3 -->
          <line x1="258" y1="64" x2="268" y2="64" stroke="#06B6D4" stroke-width="1.5" opacity="0.6"/>
          <polygon points="266,59 276,64 266,69" fill="#06B6D4" opacity="0.7"/>

          <!-- Stage 4: SCHEDULE -->
          <rect x="278" y="38" width="68" height="52" rx="8" fill="#0D2545" stroke="#06B6D4" stroke-width="1.5"><animate attributeName="fill" values="#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#06B6D4;#06B6D4;#0D2545;#0D2545" keyTimes="0;0.05;0.22;0.27;0.44;0.49;0.66;0.71;0.88;0.93;1" dur="5s" repeatCount="indefinite"/></rect>
          <text x="312" y="59" text-anchor="middle" fill="white" font-size="8" font-weight="700" font-family="Space Grotesk, sans-serif">SCHEDULE</text>
          <text x="312" y="73" text-anchor="middle" fill="rgba(255,255,255,0.65)" font-size="7.5" font-family="Space Grotesk, sans-serif">Appt. Set</text>

          <!-- Arrow 4 -->
          <line x1="348" y1="64" x2="358" y2="64" stroke="#06B6D4" stroke-width="1.5" opacity="0.6"/>
          <polygon points="356,59 366,64 356,69" fill="#06B6D4" opacity="0.7"/>

          <!-- Stage 5: DONE -->
          <rect x="368" y="38" width="46" height="52" rx="8" fill="#0D2545" stroke="#06B6D4" stroke-width="1.5"><animate attributeName="fill" values="#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#0D2545;#06B6D4;#06B6D4" keyTimes="0;0.05;0.22;0.27;0.44;0.49;0.66;0.71;0.88;0.93;1" dur="5s" repeatCount="indefinite"/></rect>
          <text x="391" y="59" text-anchor="middle" fill="white" font-size="8" font-weight="700" font-family="Space Grotesk, sans-serif">DONE</text>
          <text x="391" y="73" text-anchor="middle" fill="rgba(255,255,255,0.65)" font-size="7.5" font-family="Space Grotesk, sans-serif">Sent</text>

          <!-- Animated dot travelling the pipeline -->
          <circle cx="42" cy="64" r="5" fill="white" opacity="0.9"><animate attributeName="cx" values="42;42;132;132;222;222;312;312;391;391;42" keyTimes="0;0.05;0.22;0.27;0.44;0.49;0.66;0.71;0.88;0.93;1" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.9;0.9;0.9;0.9;0.9;0.9;0.9;0.9;0.9;0;0" keyTimes="0;0.05;0.22;0.27;0.44;0.49;0.66;0.71;0.88;0.93;1" dur="5s" repeatCount="indefinite"/></circle>

          <!-- 24/7 Clock below pipeline -->
          <!-- Clock face -->
          <circle cx="75" cy="155" r="38" fill="#0D2545" stroke="#06B6D4" stroke-width="1.5"/>
          <!-- Hour ticks -->
          <line x1="75" y1="119" x2="75" y2="124" stroke="#06B6D4" stroke-width="2" opacity="0.8"/>
          <line x1="113" y1="155" x2="108" y2="155" stroke="#06B6D4" stroke-width="2" opacity="0.8"/>
          <line x1="75" y1="191" x2="75" y2="186" stroke="#06B6D4" stroke-width="2" opacity="0.8"/>
          <line x1="37" y1="155" x2="42" y2="155" stroke="#06B6D4" stroke-width="2" opacity="0.8"/>
          <!-- Minor ticks -->
          <line x1="94" y1="122" x2="92" y2="126" stroke="#06B6D4" stroke-width="1" opacity="0.4"/>
          <line x1="109" y1="136" x2="105" y2="138" stroke="#06B6D4" stroke-width="1" opacity="0.4"/>
          <line x1="109" y1="174" x2="105" y2="172" stroke="#06B6D4" stroke-width="1" opacity="0.4"/>
          <line x1="94" y1="188" x2="92" y2="184" stroke="#06B6D4" stroke-width="1" opacity="0.4"/>
          <line x1="56" y1="188" x2="58" y2="184" stroke="#06B6D4" stroke-width="1" opacity="0.4"/>
          <line x1="41" y1="174" x2="45" y2="172" stroke="#06B6D4" stroke-width="1" opacity="0.4"/>
          <line x1="41" y1="136" x2="45" y2="138" stroke="#06B6D4" stroke-width="1" opacity="0.4"/>
          <line x1="56" y1="122" x2="58" y2="126" stroke="#06B6D4" stroke-width="1" opacity="0.4"/>
          <!-- Hour hand -->
          <line x1="75" y1="155" x2="75" y2="133" stroke="white" stroke-width="3" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" from="0 75 155" to="360 75 155" dur="12s" repeatCount="indefinite"/></line>
          <!-- Minute hand -->
          <line x1="75" y1="155" x2="75" y2="125" stroke="#06B6D4" stroke-width="2" stroke-linecap="round"><animateTransform attributeName="transform" type="rotate" from="0 75 155" to="360 75 155" dur="1.5s" repeatCount="indefinite"/></line>
          <!-- Center dot -->
          <circle cx="75" cy="155" r="3" fill="#06B6D4"/>
          <!-- 24/7 label -->
          <text x="75" y="207" text-anchor="middle" fill="rgba(255,255,255,0.5)" font-size="8" font-weight="700" font-family="Space Grotesk, sans-serif">ALWAYS ON</text>

          <!-- Human vs AI comparison -->
          <!-- Human (center) -->
          <circle cx="195" cy="143" r="13" fill="#334155"/>
          <rect x="188" y="157" width="15" height="22" rx="4" fill="#334155"/>
          <!-- Sleep ZZZ -->
          <text x="213" y="142" fill="rgba(255,255,255,0.5)" font-size="9" font-weight="700" font-family="Space Grotesk, sans-serif">Zzz</text>
          <text x="195" y="192" text-anchor="middle" fill="rgba(255,255,255,0.4)" font-size="7.5" font-family="Space Grotesk, sans-serif">9am – 5pm</text>

          <!-- AI badge (right) -->
          <circle cx="320" cy="150" r="30" fill="#0D2545" stroke="#06B6D4" stroke-width="2"><animate attributeName="r" values="28;32;28" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0.7;1;0.7" dur="2s" repeatCount="indefinite"/></circle>
          <circle cx="320" cy="150" r="22" fill="#06B6D4" opacity="0.15"><animate attributeName="r" values="22;28;22" dur="2s" repeatCount="indefinite"/></circle>
          <text x="320" y="146" text-anchor="middle" fill="#06B6D4" font-size="13" font-weight="700" font-family="Space Grotesk, sans-serif">AI</text>
          <text x="320" y="160" text-anchor="middle" fill="rgba(255,255,255,0.7)" font-size="8" font-family="Space Grotesk, sans-serif">Active</text>
          <text x="320" y="192" text-anchor="middle" fill="#06B6D4" font-size="8" font-weight="700" font-family="Space Grotesk, sans-serif">24 / 7</text>
        </svg>