<#import "/templates/system/common/crafter.ftl" as crafter />
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${errorCode} ${errorTitle} | CloudZoom Solutions</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap">
  <style>
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: #0D2545; color: #fff; font-family: "Space Grotesk", sans-serif; }
    main { text-align: center; padding: 2rem; }
    .code { font-size: 4rem; color: #06B6D4; margin: 0; }
    a { color: #06B6D4; }
  </style>
  <@crafter.head/>
</head>
<body>
<@crafter.body_top/>
<main>
  <p class="code">${errorCode}</p>
  <h1>${errorTitle}</h1>
  <p>${errorMessage}</p>
  <p><a href="/">Back to CloudZoom</a></p>
</main>
<@crafter.body_bottom/>
</body>
</html>
