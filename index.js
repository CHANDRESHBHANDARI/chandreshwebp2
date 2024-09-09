var istrue=true;
var s=0;
var m=0;
var h=0;
function set()
{
    if(istrue==true)
    {
        istrue=false;
        timer();
    }

}


function timer()
{
    if(istrue==false)
    {
        s--;
        timer.innerHTML=h+" : "+m+" : "+s;
        setTimeout("timer()",1000);
    }
}