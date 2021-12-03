import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

let opts = {
  routes: [
    {
      path: "/",
      name: "Index",
      redirect: "/task",
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/task",
      name: "Task",
      component: () => import('../views/Tasks.vue'),
      meta: {
        requiresAuth: true
      },
      children: [
        {
          path: "/editor/:id",
          name: "Editor",
          component: () => import('../views/Editor.vue'),
          meta: {
            requiresAuth: true
          }
        },
        {
          path: "/editor",
          name: "EditorCreate",
          component: () => import('../views/Editor.vue'),
          meta: {
            requiresAuth: true
          }
        },
      ]
    },
    {
      path: "/teory",
      name: "TeoryInfo",
      component: () => import('../views/Teory.vue'),
      meta: {
        requiresAuth: true
      },
      children: [
        {
          path: "/edit/:id",
          name: "TeoryEdit",
          component: () => import('../views/TeoryEdit.vue'),
          meta: {
            requiresAuth: true
          }
        },
        {
          path: "/create",
          name: "TeoryCreate",
          component: () => import('../views/TeoryEdit.vue'),
          meta: {
            requiresAuth: true
          }
        },
      ]
    },
    {
      path: "/teory/:id",
      name: "TeoryView",
      component: () => import('../views/TeoryView.vue'),
      meta: {
        requiresAuth: true
      },
    },
    // {
    //   path: "/dashboard",
    //   name: "Dashboard",
    //   component: () => import('../views/Dashboard.vue'),
    //   meta: {
    //     requiresAuth: true
    //   }
    // },
    // {
    //   path: "/websocket",
    //   name: "WebSocketSchema",
    //   component: () => import('../views/WebSocketSchemaTable.vue'),
    //   meta: {
    //     requiresAuth: true
    //   },
    //   children: [
    //     {
    //       path: "create",
    //       name: "WebSocketSchemaCreate",
    //       component: () => import('../components/modals/WebSocketSchemaModal.vue'),
    //       meta: {
    //         requiresAuth: true
    //       },
    //     },
    //     {
    //       path: "edit/:id",
    //       name: "WebSocketSchemaEdit",
    //       component: () => import('../components/modals/WebSocketSchemaModal.vue'),
    //       meta: {
    //         requiresAuth: true
    //       },
    //     },
    //   ]
    // },
    // {
    //   path: "/websocket_callback",
    //   name: "WebSocketCallback",
    //   component: () => import('../views/WebSocketCallbackTable.vue'),
    //   meta: {
    //     requiresAuth: true
    //   },
    //   children: [
    //     {
    //       path: "create",
    //       name: "WebSocketCallbackCreate",
    //       component: () => import('../components/modals/WebSocketCallbackModal.vue'),
    //       meta: {
    //         requiresAuth: true
    //       },
    //     },
    //     {
    //       path: "edit/:id",
    //       name: "WebSocketCallbackEdit",
    //       component: () => import('../components/modals/WebSocketCallbackModal.vue'),
    //       meta: {
    //         requiresAuth: true
    //       },
    //     },
    //   ]
    // },
    // {
    //   path: "/violations",
    //   name: "Violation",
    //   component: () => import('../views/ViolationsTable.vue'),
    //   meta: {
    //     requiresAuth: true
    //   },
    //   children: [
    //     {
    //       path: ":id/",
    //       name: "ViolationView",
    //       component: () => import('../components/modals/ViolationModal.vue'),
    //       meta: {
    //         requiresAuth: true
    //       },
    //     },
    //   ]
    // },
    // {
    //   path: "/settings",
    //   name: "Settings",
    //   component: () => import('../views/Settings.vue'),
    //   meta: {
    //     requiresAuth: true
    //   },
    // },
    {
      path: "/login",
      name: "login",
      component: () => import('../views/Login.vue'),
      meta: {
        requiresAuth: false
      }
    },
  ],
  linkExactActiveClass: 'active'
};
const router = new VueRouter(opts);

export default router
