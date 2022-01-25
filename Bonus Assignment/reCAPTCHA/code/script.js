(function(){
    var w=window,C='___grecaptcha_cfg',cfg=w[C]=w[C]||{},N='grecaptcha';
    var gr=w[N]=w[N]||{};gr.ready=gr.ready||function(f){(cfg['fns']=cfg['fns']||[]).push(f);
    };
    w['__recaptcha_api']='https://www.google.com/recaptcha/api2/';
    (cfg['render']=cfg['render']||[]).push('onload');
    w['__google_recaptcha_client']=true;
    var d=document,po=d.createElement('script');
    po.type='text/javascript';
    po.async=true;
    po.src='https://www.gstatic.com/recaptcha/releases/TDBxTlSsKAUm3tSIa0fwIqNu/recaptcha__en.js';
    po.crossOrigin='anonymous';
    po.integrity='sha384-HTq9bAnQeRQMZWaz4oh4hzQ7uLhEPBDMd6NizGeUQEDJ09mI0WU9lRcdix2okyzP';
    var e=d.querySelector('script[nonce]'),n=e&&(e['nonce']||e.getAttribute('nonce'));
    if(n){po.setAttribute('nonce',n);
    }
    var s=d.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(po, s);})();

var response_reCAPTCHA = grecaptcha.getClientExtensionResults();

if (response_reCAPTCHA === "success"){

    window.location.href = "https://github.com/mmsaeed509";

}else {

    alert("You can't proceed!");

}

// if (grecaptcha.getResponseHeader("success")){
//
//     function redirect(){
//         window.location.href = "https://github.com/mmsaeed509";
//     }
//
//     redirect();
//     setTimeout(Redirect, 1000);
//
// }else {
//     alert("You can't proceed!");
// }


//goto Ozil's GitHub after 4 seconds
// url = "https://github.com/mmsaeed509";
// setTimeout(()=>{
//     window.location = url;
// }, 2000);