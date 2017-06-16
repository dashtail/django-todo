import React, {StyleSheet, Dimensions, PixelRatio} from "react-native";
const {width, height, scale} = Dimensions.get("window"),
    vw = width / 100,
    vh = height / 100,
    vmin = Math.min(vw, vh),
    vmax = Math.max(vw, vh);

export default StyleSheet.create({
    "bodydragging": {
        "cursor": "move !important"
    },
    "bodydragging *": {
        "cursor": "move !important"
    },
    "dragged": {
        "position": "absolute",
        "opacity": 0.5,
        "zIndex": 2000
    },
    "olexample liplaceholder": {
        "position": "relative"
    },
    "olexample liplaceholder:before": {
        "position": "absolute"
    }
});