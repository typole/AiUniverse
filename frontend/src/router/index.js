// frontend/src/router/index.js

import Vue from 'vue';
import VueRouter from 'vue-router';
import FirstRequest from '../views/FirstRequest.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'FirstRequest',
        component: FirstRequest
    },
    // 其他路由配置...
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router;
