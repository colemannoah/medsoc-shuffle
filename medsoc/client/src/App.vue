<template>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'

import { inject } from '@vercel/analytics';

inject();
</script>
