(self.webpackChunklite=self.webpackChunklite||[]).push([[39592],{12423:(e,n,i)=>{"use strict";i.d(n,{v:()=>d});var t=i(319),a=i.n(t),l=i(77329),d={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"OverflowMenuButtonWithNegativeSignal_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"FragmentSpread",name:{kind:"Name",value:"OverflowMenuWithNegativeSignal_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"CreatorActionOverflowPopover_post"}}]}}].concat(a()([{kind:"FragmentDefinition",name:{kind:"Name",value:"OverflowMenuWithNegativeSignal_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"collection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}}]}}]),a()(l.G.definitions))}},32523:(e,n,i)=>{"use strict";i.d(n,{g:()=>l});var t=i(67294),a=i(98462),l=function(e){var n=e.children,i=e.className,l=void 0===i?"":i,d=e.href,o=e.onClick;return d?t.createElement(a.P,{className:l,href:d,onClick:o},n):n}},44346:(e,n,i)=>{"use strict";i.d(n,{S:()=>t});var t={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"NewsletterV3EmailToSubscribersMenuItem_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"newsletterV3"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"subscribersCount"}}]}}]}},{kind:"Field",name:{kind:"Name",value:"isNewsletter"}},{kind:"Field",name:{kind:"Name",value:"isAuthorNewsletter"}}]}}]}},77329:(e,n,i)=>{"use strict";i.d(n,{G:()=>s});var t=i(319),a=i.n(t),l=i(28233),d=i(10414),o=i(35963),m=i(76992),r=i(44346),s={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"CreatorActionOverflowPopover_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"allowResponses"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"statusForCollection"}},{kind:"Field",name:{kind:"Name",value:"isLocked"}},{kind:"Field",name:{kind:"Name",value:"isPublished"}},{kind:"Field",name:{kind:"Name",value:"clapCount"}},{kind:"Field",name:{kind:"Name",value:"mediumUrl"}},{kind:"Field",name:{kind:"Name",value:"pinnedAt"}},{kind:"Field",name:{kind:"Name",value:"pinnedByCreatorAt"}},{kind:"Field",name:{kind:"Name",value:"curationEligibleAt"}},{kind:"Field",name:{kind:"Name",value:"mediumUrl"}},{kind:"Field",name:{kind:"Name",value:"responseDistribution"}},{kind:"Field",name:{kind:"Name",value:"visibility"}},{kind:"FragmentSpread",name:{kind:"Name",value:"useIsPinnedInContext_post"}},{kind:"Field",name:{kind:"Name",value:"pendingCollection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"name"}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"avatar"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"domain"}},{kind:"Field",name:{kind:"Name",value:"slug"}}]}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"FragmentSpread",name:{kind:"Name",value:"MutePopoverOptions_creator"}},{kind:"FragmentSpread",name:{kind:"Name",value:"auroraHooks_publisher"}}]}},{kind:"Field",name:{kind:"Name",value:"collection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"name"}},{kind:"Field",name:{kind:"Name",value:"creator"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"avatar"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"domain"}},{kind:"Field",name:{kind:"Name",value:"slug"}},{kind:"FragmentSpread",name:{kind:"Name",value:"MutePopoverOptions_collection"}},{kind:"FragmentSpread",name:{kind:"Name",value:"auroraHooks_publisher"}}]}},{kind:"FragmentSpread",name:{kind:"Name",value:"ClapMutation_post"}},{kind:"FragmentSpread",name:{kind:"Name",value:"NewsletterV3EmailToSubscribersMenuItem_post"}}]}}].concat(a()(l.x.definitions),a()(d.m.definitions),a()(o.C.definitions),a()(d.G.definitions),a()(m.JP.definitions),a()(r.S.definitions))}},79356:(e,n,i)=>{"use strict";i.d(n,{$:()=>k,u:()=>v});var t=i(28655),a=i.n(t),l=i(71439),d=i(67294),o=i(49549),m=i(19147),r=i(32272),s=i(32262),u=i(33914);function c(){var e=a()(["\n  fragment PostFooterSocialPopover_post on Post {\n    id\n    mediumUrl\n    title\n    ...SharePostButton_post\n  }\n  ","\n"]);return c=function(){return e},e}var k=function(e){var n=e.post,i=e.source,t=n.mediumUrl,a=n.title,l=n.id;return d.createElement(m.A,{ariaId:"postFooterSocialMenu",source:{name:i},url:t,title:a,ariaLabel:"Share Post",postId:l},(function(e){return d.createElement(d.Fragment,null,d.createElement(s.Sl,{paddingTopBottom:"8px"},d.createElement(u._,{tooltipText:"Share on Twitter",targetDistance:15},d.createElement(r.f,{socialPlatform:"TWITTER",buttonStyle:"LINK_INLINE_SHORT_LABEL",post:n}))),d.createElement(s.Sl,{paddingTopBottom:"8px"},d.createElement(u._,{tooltipText:"Share on Facebook",targetDistance:15},d.createElement(r.f,{socialPlatform:"FACEBOOK",buttonStyle:"LINK_INLINE_SHORT_LABEL",post:n}))),d.createElement(s.Sl,{paddingTopBottom:"8px"},d.createElement(u._,{tooltipText:"Share on LinkedIn",targetDistance:15},d.createElement(r.f,{socialPlatform:"LINKEDIN",buttonStyle:"LINK_INLINE_SHORT_LABEL",post:n}))),t&&d.createElement(s.Sl,{paddingTopBottom:"8px"},d.createElement(u._,{tooltipText:"Copy link",targetDistance:15},d.createElement(o._,{url:t,onClick:e,reportData:{postId:n.id},source:i,copyStyle:"INLINE"}))))}))},v=(0,l.Ps)(c(),r.o)},76992:(e,n,i)=>{"use strict";i.d(n,{JP:()=>d});var t=i(319),a=i.n(t),l=i(36896),d={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"ClapMutation_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"clapCount"}},{kind:"FragmentSpread",name:{kind:"Name",value:"MultiVoteCount_post"}}]}}].concat(a()(l.U.definitions))};[{kind:"OperationDefinition",operation:"mutation",name:{kind:"Name",value:"ClapMutation"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"targetPostId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"userId"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"ID"}}}},{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"numClaps"}},type:{kind:"NonNullType",type:{kind:"NamedType",name:{kind:"Name",value:"Int"}}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"clap"},arguments:[{kind:"Argument",name:{kind:"Name",value:"targetPostId"},value:{kind:"Variable",name:{kind:"Name",value:"targetPostId"}}},{kind:"Argument",name:{kind:"Name",value:"userId"},value:{kind:"Variable",name:{kind:"Name",value:"userId"}}},{kind:"Argument",name:{kind:"Name",value:"numClaps"},value:{kind:"Variable",name:{kind:"Name",value:"numClaps"}}}],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"viewerEdge"},selectionSet:{kind:"SelectionSet",selections:[{kind:"FragmentSpread",name:{kind:"Name",value:"ClapMutation_viewerEdge"}}]}},{kind:"FragmentSpread",name:{kind:"Name",value:"ClapMutation_post"}}]}}]}}].concat(a()([{kind:"FragmentDefinition",name:{kind:"Name",value:"ClapMutation_viewerEdge"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"PostViewerEdge"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"clapCount"}}]}}]),a()(d.definitions))},36896:(e,n,i)=>{"use strict";i.d(n,{U:()=>a});var t=i(319),a={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"MultiVoteCount_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"FragmentSpread",name:{kind:"Name",value:"PostVotersNetwork_post"}}]}}].concat(i.n(t)()([{kind:"FragmentDefinition",name:{kind:"Name",value:"PostVotersNetwork_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"voterCount"}},{kind:"Field",name:{kind:"Name",value:"recommenders"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"name"}}]}}]}}]))}},50077:(e,n,i)=>{"use strict";i.d(n,{Q5:()=>B,u_:()=>O,yu:()=>M,Gk:()=>K});var t=i(28655),a=i.n(t),l=i(63038),d=i.n(l),o=i(71439),m=i(67294),r=i(83687),s=i(36823),u=i(10734),c=i(32523),k=i(95482),v=i(92013),p=i(31635),N=i(9292),S=i(41832),f=i(82143),F=i(52862),E=i(98024),g=i(98701),_=i(77180),C=i(6688),y=i(7650),h=i(61598);function P(){var e=a()(["\n  fragment CardByline_publisher on Publisher {\n    __typename\n    ... on User {\n      id\n      ...CardByline_user\n    }\n    ... on Collection {\n      id\n      ...CardByline_collection\n    }\n  }\n  ","\n  ","\n"]);return P=function(){return e},e}function I(){var e=a()(["\n  fragment CardByline_collection on Collection {\n    __typename\n    id\n    name\n    ...collectionUrl_collection\n  }\n  ","\n"]);return I=function(){return e},e}function D(){var e=a()(["\n  fragment CardByline_user on User {\n    __typename\n    id\n    name\n    username\n    mediumMemberAt\n    socialStats {\n      followerCount\n    }\n    ...userUrl_user\n    ...UserMentionTooltip_user\n  }\n  ","\n  ","\n"]);return D=function(){return e},e}function b(){var e=a()(["\n  fragment CardByline_post on Post {\n    ...DraftStatus_post\n  }\n  ","\n"]);return b=function(){return e},e}var T=function(e){return{fill:e.baseColor.fill.light,marginTop:"-2px",paddingLeft:"4px"}};function L(e,n){return n&&(0,g.nE)(e)?e[n]:e}var w=function(e){var n=e.author,i=e.forceSize,t=e.scale,a=void 0===t?"M":t,l=m.useState(0),o=d()(l,2),r=o[0],u=o[1],k=(0,_.F)(),v=(0,s.B)(n);if(m.useEffect((function(){r||u(window.innerWidth)}),[]),!n||!n.name)return null;var p=r<=k.breakpoints.sm,N=m.createElement(c.g,{href:v},m.createElement(E.F,{color:"ACCENT",scale:L(a,i)},n.name));return p?N:m.createElement(F.$,{placement:"right",targetDistance:15,mouseLeaveDelay:200,popoverRenderFn:function(){return m.createElement(S.K,{user:n})}},N)},A=function(e){var n=e.collection,i=e.forceSize,t=e.scale,a=void 0===t?"M":t,l=(0,r.R)(n);return m.createElement(c.g,{href:l},m.createElement(E.F,{scale:L(a,i),color:"DARKER"},"Published in ",m.createElement(u.t,{collection:n})))},x=function(e){var n=e.small,i=void 0!==n&&n,t=e.hideDot,a=void 0!==t&&t,l=(0,C.I)();return m.createElement("span",{className:l({margin:"0 ".concat(i?4:7,"px")})},a?null:"·")},B=function(e){var n=e.datePrefix,i=void 0===n?"":n,t=e.forceSize,a=e.isOneLine,l=e.withMidDot,d=void 0===l||l,o=e.href,r=e.onClick,s=e.publishedAt,u=e.scale,N=void 0===u?"M":u,S=e.showStar,f=void 0!==S&&S,F=e.showPinned,g=void 0!==F&&F,_=e.timeColor,h=void 0===_?"LIGHTER":_,P=e.timeToRead,I=e.post,D=(0,C.I)();if(!s&&!P)return null;var b=a?v.h:k.E;return m.createElement(c.g,{href:o,onClick:r},m.createElement(E.F,{color:h,scale:L(N,t)},a&&d&&m.createElement(x,{small:!0,hideDot:!!P&&!!s}),s&&!g?m.createElement(m.Fragment,null,i,m.createElement(b,{hasPrefix:!(!a||!i)||void 0,timestamp:s})):null,g?m.createElement("span",null,"Pinned"):null,s&&P?m.createElement(x,null):null,P||null,!s&&m.createElement(m.Fragment,null,m.createElement(x,{small:a}),m.createElement(E.F,{color:"DARKER",scale:L(N,t),tag:"span"},m.createElement(p.FV,{post:I}))),f&&m.createElement(y.Z,{className:D(T)})))},O=function(e){var n=e.avatar,i=void 0===n?null:n,t=e.datePrefix,a=e.forceSize,l=e.hideAuthor,d=void 0!==l&&l,o=e.href,r=e.onClick,s=e.isOneLine,u=void 0!==s&&s,c=e.publisher,k=e.publishedAt,v=e.scale,p=e.showStar,S=void 0!==p&&p,f=e.showPinned,F=void 0!==f&&f,E=e.timeColor,g=e.timeToRead,_=e.post,C="Collection"===c.__typename?m.createElement(A,{collection:c,forceSize:a,scale:v}):d?null:m.createElement(w,{author:c,forceSize:a,scale:v}),y="Collection"===c.__typename||!d;return m.createElement(N.Y,{avatar:d?null:i,isOneLine:u,title:C,description:m.createElement(B,{datePrefix:t,publishedAt:k,timeToRead:g,withMidDot:y,href:o,onClick:r,showStar:S,showPinned:F,forceSize:a,scale:v,timeColor:E,isOneLine:u,post:_})})},M=(0,o.Ps)(b(),p.tV),V=(0,o.Ps)(D(),h.$m,f.O),R=(0,o.Ps)(I(),h.nf),K=(0,o.Ps)(P(),V,R)},35963:(e,n,i)=>{"use strict";i.d(n,{C:()=>t});var t={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"auroraHooks_publisher"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Publisher"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"__typename"}},{kind:"InlineFragment",typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Collection"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"isAuroraEligible"}},{kind:"Field",name:{kind:"Name",value:"isAuroraVisible"}},{kind:"Field",name:{kind:"Name",value:"viewerEdge"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"isEditor"}}]}}]}},{kind:"InlineFragment",typeCondition:{kind:"NamedType",name:{kind:"Name",value:"User"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"isAuroraVisible"}}]}}]}}]}},28233:(e,n,i)=>{"use strict";i.d(n,{x:()=>t});var t={kind:"Document",definitions:[{kind:"FragmentDefinition",name:{kind:"Name",value:"useIsPinnedInContext_post"},typeCondition:{kind:"NamedType",name:{kind:"Name",value:"Post"}},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}},{kind:"Field",name:{kind:"Name",value:"collection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"pendingCollection"},selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"id"}}]}},{kind:"Field",name:{kind:"Name",value:"pinnedAt"}},{kind:"Field",name:{kind:"Name",value:"pinnedByCreatorAt"}}]}}]}},32272:(e,n,i)=>{"use strict";i.d(n,{f:()=>k,o:()=>v});var t=i(28655),a=i.n(t),l=i(71439),d=i(67294),o=i(24862),m=i(95760),r=i(51512),s=i(67297),u=i(27952);function c(){var e=a()(["\n  fragment SharePostButton_post on Post {\n    id\n  }\n"]);return c=function(){return e},e}var k=function(e){var n,i=e.post,t=e.socialPlatform,a=e.buttonStyle,l=(0,m.Av)(),c=(0,r.Qi)(),k=(0,s.v9)((function(e){return e.config.authDomain}));if("FACEBOOK"===t)n=(0,u.VCf)(k,i.id);else if("TWITTER"===t)n=(0,u.A2M)(k,i.id);else{if("LINKEDIN"!==t)return null;n=(0,u.mZD)(k,i.id)}return d.createElement(o.T,{baseOnClick:function(){c&&l.event("post.shareOpen",{postId:i.id,source:c,dest:t.toLowerCase(),dialogType:"native"})},href:n,socialPlatform:t,buttonStyle:a})},v=(0,l.Ps)(c())},14071:(e,n,i)=>{"use strict";i.d(n,{E:()=>k,U:()=>v});var t=i(28655),a=i.n(t),l=i(71439),d=i(67294),o=i(49549),m=i(32272),r=i(42933),s=i(33914),u=i(51512);function c(){var e=a()(["\n  fragment SharePostButtons_post on Post {\n    id\n    isLimitedState\n    visibility\n    mediumUrl\n    ...SharePostButton_post\n  }\n  ","\n"]);return c=function(){return e},e}var k=(0,l.Ps)(c(),m.o);function v(e){var n=e.post,i=e.source,t="UNLISTED"===n.visibility;return d.createElement(d.Fragment,null,d.createElement(u.cW,{source:{name:i}},d.createElement(r.x,{flexGrow:"0",paddingRight:"1px"},!t&&d.createElement(s._,{tooltipText:"Share on Twitter",targetDistance:15},d.createElement(m.f,{socialPlatform:"TWITTER",buttonStyle:n.isLimitedState?"LINK_DISABLED":"LINK",post:n}))),d.createElement(r.x,{flexGrow:"0",paddingRight:"1px"},!t&&d.createElement(s._,{tooltipText:"Share on Facebook",targetDistance:15},d.createElement(m.f,{socialPlatform:"FACEBOOK",buttonStyle:n.isLimitedState?"LINK_DISABLED":"LINK",post:n}))),d.createElement(r.x,{flexGrow:"0",paddingRight:"1px"},!t&&d.createElement(s._,{tooltipText:"Share on LinkedIn",targetDistance:15},d.createElement(m.f,{socialPlatform:"LINKEDIN",buttonStyle:n.isLimitedState?"LINK_DISABLED":"LINK",post:n})))),d.createElement(r.x,{flexGrow:"0"},!t&&n.mediumUrl&&d.createElement(s._,{tooltipText:"Copy link",targetDistance:15},d.createElement(o._,{url:n.mediumUrl,copyStyle:n.isLimitedState?"ICON_DISABLED":"ICON",source:i,reportData:{postId:n.id}}))))}}}]);
//# sourceMappingURL=https://stats.medium.build/lite/sourcemaps/39592.4b817af2.chunk.js.map