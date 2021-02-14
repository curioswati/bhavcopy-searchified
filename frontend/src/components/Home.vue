<template>
    <div class="home">
        <Search @loadRecords="result=$event"/>
        <Results v-if="result.records" :result="result"/>
    </div>
</template>

<script>

import Search from '../components/Search';
import Results from '../components/Results';
import axios from 'axios';

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
    methods: {
        loadRecords: function() {
            axios.get('/api/').then(
                response => {
                    this.result = response.data;

                    // store the latest records' data in localStorage to load when there is no stock searched
                    localStorage.setItem("result", JSON.stringify(response.data));
                }
            );
        }
    },
    created: function() {
        this.loadRecords();
    }
}
</script>

<style scoped>
    .home {
        min-height: 750px;
    }
</style>
