<template>
  <div class='main'>
    <el-radio-group v-model="radio1">
      <el-radio label="1" >Option 1</el-radio>
      <el-radio label="2" >Option 2</el-radio>
    </el-radio-group>
    <div>{{radio1}}</div>

    <!-- day6 -->
    <el-divider>
      <h2>
        day6
      </h2>
    </el-divider>
    <ul>
      <li v-for="(item,index) in list1" :key="index">
        {{item}}
      </li>
    </ul>

    <el-button
      v-on:click="print()"
    >
      button
    </el-button>

    <el-button
      @click="print()"
    >
      button
    </el-button>

    <div v-if="true">hello</div>






  </div>
</template>

<script lang="ts" setup>
import { computed, ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore, mapState, mapMutations } from 'vuex'
import axios from 'axios'


// vuex ############################
const store = useStore()


// route ###########################
const route = useRoute()
const router = useRouter()

// radio
const radio1 = ref('1')
let label1="1"

// list 
let list1=[0,1,2,3]

const print=()=>{
  console.log('hello')
}

onMounted(() => {
  console.log('hello world')
})

const callFunction1=()=>{
  axios.get('',{
    params:{
      param1:'hey'
    }
  })
  .then(res=>{
    console.log(res.data['msg'])
  })
}


</script>

<style lang="scss" scoped>
.main{
  width:80vw;
  margin: 0 auto;
}

</style>
