# Abstract:
When the brute-force target is a simple FTP or a Telnet, its easy to perform a brute-force on, than on doing the same on web logins. Especially modern webpages that are based on JS logins. The brute-force app has to manage cookies, browser information, hidden fields etc. Burp-Suite can handle these things majority of the times, but so can browser automation techniques, where the browser does the same tasks an user would do to brute-force, thus making it simple to run without any technical hassle. Such program already exists. And the famous one is called Hatch.

Making such tools are possible with integrations like selenium and I have previously made this type of tools. But the problem was that, it would only be website specific, where I would have to hard code the username, password, otp or whatever HTML elements there is, and then run the program. So this time I wanted it to be dynamic, where you have to manually give the form information at run-time, thus making the program dynamic and applicable to majority of web sites, and found out, that Hatch already does that for you.

The only thing that was missing in hatch, that burp-suite handles like a charm is, positional arguments, that is, you might not want to just brute-force the username and password. Maybe its an OTP or there is a third field on the login form. So thats going to have to be dynamically asked at run-time, and thats what Hatch doesnt have. So I just made an extension out of it, where like Hatch, you can brute-force through the browser itself, but not only static to user name and password, but any number of iterative or static fields within a form that you want to add. So in brief. This tool allows you to add any number of bruteforce positions like on Burpsuite, but does the job like Hatch in the end. 

#Usage:

The usage is pretty much simple. You need to have the selenium on your computer and that's the only dependency. Except that, download the chrome driver, that matches the version of Google Chrome installed on your computer. Keep it anywhere. The rest of usage is within the program, and it will prompt and exactly ask what it needs, so its pretty straight forward. 

Thank you for using it ...
