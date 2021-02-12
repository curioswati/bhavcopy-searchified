<template>
    <div class="home">
        <Search @loadRecords="result=$event"/>
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
}
</script>

<style scoped>
    .home {
        min-height: 750px;
    }
</style>
