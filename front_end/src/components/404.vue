<template>
  <div>
    <h1>404</h1>

  </div>
</template>

<script lang="ts" setup>
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore, mapState, mapMutations } from 'vuex'
//import axios from 'axios'


// vuex ############################
const store = useStore()


// route ###########################
const route = useRoute()
const router = useRouter()


</script>

<style lang="scss" scoped>


</style>