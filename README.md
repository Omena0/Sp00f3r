
# SP00F3R

Tool to spoof file extensions of .py files.

Your payload will most likely be executed.

# How we do it

The spoofing process consists of 4 steps.

## Step 1

### Build to exe

This will make sure your payload can run on machines that dont have python installed.

## Step 2

### Spoof extension

We rename the .exe to .scr because .exe is alot more suspicious than the less know .scr file, even though they are the same.

Using a special unicode character [`U-202E`] we reverse the file extension, so we can set it as ANYTHING we want.

Imagine you have a file called `runme.exe`. When you double click it, you KNOW you're running the file.

But when we spoof the extension, it'll look like `cktuajozyxjircs.zip`

Its an archive, right?

### ITS NOT

But how?

The `U-202E` Character renders all text after it from RIGHT TO LEFT, effectively flipping it.

Now if you look at the file again, just before the .png theres `rcs`, whats the reverse of that? `scr`! ITS A SCREENSAVER!

As i told before the `.scr` and `.exe` extensions are the exact same, the `.scr` one is just used commonly with screensavers. You can rename ANY `.exe` to `.scr` and it'll work normally.

### But why the gibberish?

We're using a bunch of random letters because that hides the true extension.

What else would you name it? novirus_rcs.zip? Already suspicious as hell.

### Step 3

We set the icon to the image we are spoofing to be.

### Step 4

[DO THIS MANUALLY]

But what now? I thought we already spoofed the extension?

Simple,

We archive the spoofed exe.

### But why?

All programs might not support `U-202E`'s text flipping (or remove it), so when the target downloads the file they would see that its actually an exe.

But if we put it in a `.zip` file, they wont see the spoofed exe in their web browser, ect. The only place they will see it is in windows file explorer. Which supports `U-202E`.

This works especially well if you include multiple files and folders.

### Covering Up

Before every payload, we include a small `SELF EXTRACTING FILE` that stores the data of the spoofed png, and on open, writes it to a temp file that is then opened. This way the target wont think anything of the `.png` as it opens normally unless they try to write to it or see the file path of course but thats unlikely. And at that point it's already too late, as `your payload` has already executed.

Also because its a `.scr` file it shows extra options for installing the screensaver, if you click ANY of them, the payload runs as well, but its way more obvious

<br><br><br><br><br><br>

# DISCLAIMER

I AM NOT RESPONSIBLE FOR WHATEVER THE FUCK YOU DO WITH THIS

I CREATED THIS TOOL FOR ONLY EDUCATIONAL AND PENTESTING PURPOSES!

DO NOT SEND MALICIOUS FILES TO ANYONE WITHOUT PRIOR CONSENT
