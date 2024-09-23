<template>
  <Analytics />
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
import { Analytics } from "@vercel/analytics/react"
</script>
