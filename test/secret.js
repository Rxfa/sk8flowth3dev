console.log("password12ffff3");
document.cookie = "username=John Doe; expires=Sun, 15 Jan 2022 10:19:00 UTC;path=/;";
document.cookie = "admin=true;path=/;";
document.cookie = "banned=false;path=/;";
document.cookie = "username=John Doe; expires=Sun, 15 Jan 2022 10:22:00 UTC;path=/;";
document.cookie = "name=John Doe; expires=Sun, 15 Jan 2022 10:23:00 UTC;path=/;";
document.cookie = "username=John Doe; expires=Sun, 15 Jan 2022 10:30:00 UTC;path=/;";
document.cookie = "xxxx=John Doe; expires=Sun, 15 Jan 2022 10:49:00 UTC;path=/;";

console.log(document.cookie);
let ss = document.cookie[6] + document.cookie[7] + document.cookie[8] + document.cookie[9];
if(ss == "true"){
    alert("works");
}
//if(document.cookie[6:10])