import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    partoneData : [],
    parttwoData : [],
    partthreeData : [],
    partfourData : [],
    partfiveData : [],
    partsixData : []
  },
  mutations: {
    GetPartOneData(state,data){
      state.partoneData = data;
    },
    GetPartTwoData(state,data){
      state.parttwoData = data;
    },
    GetPartThreeData(state,data){
      state.partthreeData = data;
    },
    GetPartFourData(state,data){
      state.partfourData = data;
    },
    GetPartFiveData(state,data){
      state.partfiveData = data;
    },
    GetPartSixData(state,data){
      state.partsixData = data;
    }
  },
  getters : {
    // movie : function(state){
    //   return state.movie;
    // }
  },
  actions: {
    // update({commit},data){
    //   setTimeout(()=>{
    //     commit('Update', n);
    // },3000);
    // }
  },
  modules: {
  }
})
