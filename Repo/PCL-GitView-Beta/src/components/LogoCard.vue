<script setup>
defineProps({
    scale: Number,
    shadow: {
        type: Boolean,
        default: true,
    },
});
</script>

<template>
    <div class="cardcontainer" :style="{ transform: `scale(${scale})` }">
        <div class="blur" v-if="shadow"></div>
        <span></span>
    </div>
</template>

<style scoped lang="less">
div.cardcontainer {
    width: 735px;
    height: 735px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    position: relative;
    div.blur {
        position: absolute;
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background: linear-gradient(to bottom right, #127aef 50%, #002b5b 50%);
        filter: blur(100px);
    }
    span {
        z-index: 1;
        width: calc(calc(100% - 157.5px) / 1.5);
        height: calc(100% / 1.5);
        transform: rotate(-7deg);
        background-image: url("../assets/logocard.webp");
        background-size: 100% 100%;
    }
}
</style>
