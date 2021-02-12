<template>
    <div class="home">
        <Search @loadRecords="result=$event"/>
        <Results v-if="result.records" :result="result"/>
    </div>
</template>

<script>

import Search from '../components/Search';
import Results from '../components/Results';

export default {
  name: 'Home',
  components: {
    Search,
    Results,
  },
  data: function () {
    return {
        result: {}
    }
  },
}
</script>

<style scoped>
    .home {
        min-height: 750px;
    }
</style>
