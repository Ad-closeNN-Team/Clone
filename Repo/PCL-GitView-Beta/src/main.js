// Create App
import { createApp } from "vue";
import App from "./App.vue";
import "./assets/main.css";
const app = createApp(App);

// Plugin Loading
import router from "./router";
app.use(router);
// =============== //
import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "element-plus/theme-chalk/dark/css-vars.css";
import zhCn from "element-plus/es/locale/lang/zh-cn";
app.use(ElementPlus, {
    locale: zhCn,
});
import * as ElementPlusIconsVue from "@element-plus/icons-vue";
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component);
}
import "dayjs/locale/zh-cn";

// Mount
app.mount("#app");

// Theme Change Detector
const matchTheme = (e) => {
    if (e.matches) {
        document.documentElement.classList.add("dark");
    } else {
        document.documentElement.classList.remove("dark");
    }
};
window
    .matchMedia("(prefers-color-scheme: dark)")
    .addEventListener("change", matchTheme);
matchTheme(window.matchMedia("(prefers-color-scheme: dark)"));
