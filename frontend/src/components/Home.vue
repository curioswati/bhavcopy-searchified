<template>
    <div class="home">
        <Bhavcopy />
        <Results />
    </div>
</template>

<script>

import Bhavcopy from '../components/Bhavcopy';
import Results from '../components/Results';

export default {
  name: 'Home',
  components: {
    Bhavcopy,
    Results,
  },
}
</script>

<style scoped>
    .home {
        min-height: 750px;
    }
</style>
