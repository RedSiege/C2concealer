
'''
#############################################################################
Data set containing three elements, a list of js, css and html objects to use
to prepend a getServer reply with. getServer replies are the C2 control 
commands issued by the operator via Cobalt Strike. The data here can be 
anything really...basically any normal-ish server response would make sense.
We stuck with html, css and js just to make life easier. But be creative.

If you add a new file type, you'll need to edit the logic on line 51 of
/components/getserver.py. Right now, it's only built for html, js and css.

Note: when you add to this, make sure your outer string is created using ""
and not ''. Cobalt Strike will convert it to "" no matter what you use.
As a result, you'll want to escape all of your \' in the actual string + 
change any " to \'. If you don't do this, you'll generate a ton of errors
when trying to use c2lint.
#############################################################################

'''

#CUSTOMIZE WITH OTHER COMMON JS FILE BEGINNINGS#
js = [

##Start jquery v3.4.1##
"/*! jQuery v3.4.1 | (c) JS Foundation and other contributors | jquery.org/license */\
!function(e,t){\'use strict\';\'object\'==typeof module&&\'object\'==typeof module.exports?\
module.exports=e.document?t(e,!0):function(e){if(!e.document)throw new Error(\'jQuery \
requires a window with a document\');return t(e)}:t(e)}(\'undefined\'!=typeof window?window\
:this,function(C,e){\'use strict\';var t=[],E=C.document,r=Object.getPrototypeOf,s=t.slice\
,g=t.concat,u=t.push,i=t.indexOf,n={},o=n.toString,v=n.hasOwnProperty,a=v.toString,l=\
a.call(Object),y={},m=function(e){return\'function\'==typeof e&&\'number\'!=typeof e.nodeType}\
,x=function(e){return null!=e&&e===e.window},c={type:!0,src:!0,nonce:!0,noModule:!0};fun\
ction b(e,t,n){var r,i,o=(n=n||E).createElement(\'script\');if(o.text=e,t)for(r in c)(i=t[\
r]||t.getAttribute&&t.getAttribute(r))&&o.setAttribute(r,i);n.head.appendChild(o).parentNode;"
##End jquery v3.4.1##
,
##Start jquery ui v1.12.1##
"/*! jQuery UI - v1.12.1 - 2016-09-14\
* http://jqueryui.com\
* Includes: widget.js, position.js,\
 data.js, disable-selection.js, effect.js, effects/effect-blind.js, effects/effect-bounce.js\
 , effects/effect-clip.js, effects/effect-drop.js, effects/effect-explode.js, effects/effect\
 -fade.js, effects/effect-fold.js, effects/effect-highlight.js, effects/effect-puff.js, effe\
 cts/effect-pulsate.js, effects/effect-scale.js, effects/effect-shake.js, effects/effect-s\
 ize.js, effects/effect-slide.js, effects/effect-transfer.js, focusable.js, form-reset-mix\
 in.js, jquery-1-7.js, keycode.js, labels.js, scroll-parent.js, tabbable.js, unique-id.js,\
  widgets/accordion.js, widgets/autocomplete.js, widgets/button.js, widgets/checkboxradio.\
  js, widgets/controlgroup.js, widgets/datepicker.js, widgets/dialog.js, widgets/draggable\
  .js, widgets/droppable.js, widgets/menu.js, widgets/mouse.js, widgets/progressbar.js, w\
  idgets/resizable.js, widgets/selectable.js, widgets/selectmenu.js, widgets/slider.js, w\
  idgets/sortable.js, widgets/spinner.js, widgets/tabs.js, widgets/tooltip.js\
* Copyright jQuery Foundation and other contributors; Licensed MIT */"
##End jquery ui v1.12.1##
,
##Start jquery v2.2.4##
"/*! jQuery v2.2.4 | (c) jQuery Foundation | jquery.org/license */\
!function(a,b){\'object\'==typeof module&&\'object\'==typeof module.exp\
orts?module.exports=a.document?b(a,!0):function(a){if(!a.document)th\
row new Error(\'jQuery requires a window with a document\');return b(a\
)}:b(a)}(\'undefined\'!=typeof window?window:this,function(a,b){var c=\
[],d=a.document,e=c.slice,f=c.concat,g=c.push,h=c.indexOf,i={},j=i.t\
oString,k=i.hasOwnProperty,l={},m=\'2.2.4\',n=function(a,b){return new \
n.fn.init(a,b)},o=/^[suFEFFxA0]+|[suFEFFxA0]+$/g,p=/^-ms-/,q=/-\
([da-z])/gi,r=function(a,b){return b.toUpperCase()};n.fn=n.prototype\
={jquery:m,constructor:n,selector:\'\',length:0,toArray:function(){retu\
rn e.call(this)},get:function(a){return null!=a?0>a?this[a+this.lengt\
h]:this[a]:e.call(this)},pushStack:function(a){var b=n.merge(this.con\
structor(),a);return b.prevObject=this,b.context=this.context,b},each:"
##End jquery v2.2.4##
] 

#CUSTOMIZE WITH ADDITIONAL CSS FILE BEGINNINGS#
css = [

##Start WP Authority-Pro CSS##
"html{line-height:1.15;-webkit-text-size-adjust:100%}body{margin:0}main{dis\
play:block}h1{font-size:2em;margin:.67em 0}hr{box-sizing:content-box;height\
:0;overflow:visible}pre{font-family:monospace,monospace;font-size:1em}a{bac\
kground-color:transparent}abbr[title]{border-bottom:none;text-decoration:un\
derline;text-decoration:underline dotted}b,strong{font-weight:bolder}code,k\
bd,samp{font-family:monospace,monospace;font-size:1em}small{font-size:80%}su\
b,sup{font-size:75%;line-height:0;position:relative;vertical-align:baseline}\
sub{bottom:-.25em}sup{top:-.5em}img{border-style:none}button,input,optgroup,\
select,textarea{font-family:inherit;font-size:100%;line-height:1.15;margin:0\
}button,input{overflow:visible}button,select{text-transform:none}[type=butto\
n],[type=reset],[type=submit],button{-webkit-appearance:button}[type=button]\
::-moz-focus-inner,[type=reset]::-moz-focus-inner,[type=submit]::-moz-focus-\
inner,button::-moz-focus-inner{border-style:none;padding:0}[type=button]:-m"
##End WP Authority-Pro CSS##
,
##Start https://fast.fonts.net/cssapi/6e7eef0e-28ec-43c0-a707-f08a1eb1c6b9.css?ver=4.8.3##
"@import url(/t/1.css?apiType=css&projectid=6e7eef0e-28ec-43c0-a707-f08a1eb1c6b9);\
@font-face{\
font-family:\'StymieW01-BoldCondensed\';\
src:url(\'/dv2/2/d06fb800-a3e7-4a04-b8b8-a1f5d23f4439.eot?d44f19a684109620e4841579ae\
90e818937f0df4d514ffe0d3e3e57723a4125208f710b15d5bd87a20be5922b56a3a06b0f26ae7d9305\
83a24007f936f67b82ff92d0c643f2b648064a59cc1c28679e075ed12931c5b949e1e9478c09bb8b5fb\
94f462c6c3a419e45e785b0869&projectId=6e7eef0e-28ec-43c0-a707-f08a1eb1c6b9#iefix\');\
src:url(\'/dv2/2/d06fb800-a3e7-4a04-b8b8-a1f5d23f4439.eot?d44f19a684109620e4841579ae\
90e818937f0df4d514ffe0d3e3e57723a4125208f710b15d5bd87a20be5922b56a3a06b0f26ae7d9305\
83a24007f936f67b82ff92d0c643f2b648064a59cc1c28679e075ed12931c5b949e1e9478c09bb8b5fb\
94f462c6c3a419e45e785b0869&projectId=6e7eef0e-28ec-43c0-a707-f08a1eb1c6b9#iefix\') f\
ormat(\'eot\'),url(\'/dv2/14/917cefa0-8659-4ad4-a4bf-b0ec714d1cfb.woff2?d44f19a6841096\
20e4841579ae90e818937f0df4d514ffe0d3e3e57723a4125208f710b15d5bd87a20be5922b56a3a06b\
0f26ae7d930583a24007f936f67b82ff92d0c643f2b648064a59cc1c28679e075ed12931c5b949e1e94\
78c09bb8b5fb94f462c6c3a419e45e785b0869&projectId=6e7eef0e-28ec-43c0-a707-f08a1eb1c6\
b9\') format(\'woff2\'),url(\'/dv2/3/065df875-84bb-45cd-afa3-d42b170797be.woff?d44f19a6\
84109620e4841579ae90e818937f0df4d514ffe0d3e3e57723a4125208f710b15d5bd87a20be5922b56\
a3a06b0f26ae7d930583a24007f936f67b82ff92d0c643f2b648064a59cc1c28679e075ed12931c5b94\
9e1e9478c09bb8b5fb94f462c6c3a419e45e785b0869&projectId=6e7eef0e-28ec-43c0-a707-f08a\
1eb1c6b9\') format(\'woff\'),url(\'/dv2/1/cababd22-b9ea-4e13-90dd-cd914957484d.ttf?d44f\
19a684109620e4841579ae90e818937f0df4d514ffe0d3e3e57723a4125208f710b15d5bd87a20be592\
2b56a3a06b0f26ae7d930583a24007f936f67b82ff92d0c643f2b648064a59cc1c28679e075ed12931c\
5b949e1e9478c09bb8b5fb94f462c6c3a419e45e785b0869&projectId=6e"
##End https://fast.fonts.net/cssapi/6e7eef0e-28ec-43c0-a707-f08a1eb1c6b9.css?ver=4.8.3##

]

#CUSTOMIZE WITH ADDITIONAL HTML FILE BEGINNINGS#
html = [

##Start www.bbcamerica.com cleaned up## 
"<!DOCTYPE html>\
<html class=\'no-js\' lang=\'en-US\'>\
  <head>\
    <meta http-equiv=\'X-UA-Compatible\' content=\'IE=EDGE\' />\
    <meta charset=\'utf-8\'>\
    <meta name=\'viewport\' content=\'width=device-width, initial-scale=1\' />\
    <meta name=\'apple-itunes-app\' content=\'app-id=1089249069\'>\
    <title>Untitled</title>\
<meta name=\'description\' content=\'"
##END www.bbcamerica.com cleaned##
,
##START sonymusic.com cleaned up##
"<!DOCTYPE html>\
<!--[if IE 7]><html class=\'ie ie7\' lang=\'en-US\'><![endif]-->\
<!--[if IE 8]><html class=\'ie ie8\' lang=\'en-US\'><![endif]-->\
<!--[if !(IE 7) | !(IE 8)  ]><!--><html lang=\'en-US\'><!--<![endif]-->\
    <head>\
        <meta charset=\'UTF-8\' />\
        <meta name=\'viewport\' content=\'width=device-width\' />\
        <title>\
            Official Website        </title>\
        <meta name=\'description\' content=\'Official Website\' />\
        <meta name=\'keywords\' content=\'Entertainment\' />\
                    <meta property=\'og:title\' content=\'\' />\
            <meta property=\'og:url\' content=\'https://www."
##END sonymusic.com cleaned up##
]