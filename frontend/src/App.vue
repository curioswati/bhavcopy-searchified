<template>
  <div id="app">
      <Header />
      <Home />
      <Footer />
  </div>
</template>

<script>

import Header from './components/Header';
import Home from './components/Home';
import Footer from './components/Footer';

export default {
  name: 'App',
  components: {
      Header,
      Home,
      Footer,
  },
  created: function () {
      document.title = 'Bhavcopy Searchified';
  }
}
</script>

<style>

    .bg-site-primary {
        background: lightgreen !important;
    }

</style>
