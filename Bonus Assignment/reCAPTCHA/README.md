<h1 align="center">Image CAPTCHA (Google reCAPTCHA) </h1>

> :warning: **[use WebStorm IDE](https://www.jetbrains.com/webstorm/) as it creates a localhost server auto**

[Create reCAPTCHA](#create-recaptcha)

![](reCAPTCHA.webp)

# Create reCAPTCHA
Create your [reCAPTCHA](https://www.google.com/recaptcha/admin/create) 

![](https://github.com/mmsaeed509/Information-and-Computer-Network-Security/blob/cdbd2ec840caa0ce0b3e2b55ca19ad7656c77dc7/Bonus%20Assignment/reCAPTCHA/Images/domain.png)

site key

![](https://github.com/mmsaeed509/Information-and-Computer-Network-Security/blob/cdbd2ec840caa0ce0b3e2b55ca19ad7656c77dc7/Bonus%20Assignment/reCAPTCHA/Images/siteKey.png)

open client side integration


```html
<html>
  <head>
    <title>reCAPTCHA demo: Simple page</title>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>
  </head>
  <body>
    <form action="?" method="POST">
      <div class="g-recaptcha" data-sitekey="your_site_key"></div>
      <br/>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
```
this code you need only 2 lines

first line

```html

<script src="https://www.google.com/recaptcha/api.js" async defer></script>

```

add this line into your html file in the `<head></head>` as shown below (from my HTML File)

```html

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ozoz Captcha in JavaScript </title>
    <link rel="stylesheet" href="style.css">
  
    <!-- reCAPTCHA  -->
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

    <script src="https://www.google.com/recaptcha/api/siteverify" async defer></script>


    <!-- Font Awesome CDN Link for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
</head>

```
the second one 

```html

<div class="g-recaptcha" data-sitekey="your_site_key"></div>

```

add this line into your html file in the `<body></body>` as shown below (from my HTML File) with [SITE KEY](#site-key)

```html

<body>
<div class="wrapper">
    <header>Ozoz GitHub reCAPTCHA</header>

    <div class="g-recaptcha" data-sitekey="6LfnjDUeAAAAACBFuJxYV9Rvv7poGmtZjK4LQj28"></div>

    <div class="status-text"></div>
</div>

<script src="script.js"></script>

</body>

```




