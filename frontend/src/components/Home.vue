<template>
    <div class="home">
        <Search @loadRecords="result=$event"/>
        <Results v-if="result.records.length > 0" :result="result"/>

        <div v-else class="container">
            <div class="row">
                <div class="col-md-12">
                <p class="msg text-danger">
                <span>There was some problem in fetching latest records from BSE.</span>
                <br>
                <span>You can still search for a specific stock above and get old records.</span>
                </p>
                </div>
            </div>
        </div>
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
            this.result = JSON.parse(localStorage.getItem("result"));

            if (this.result == null || this.result.records.length < 1) {
                axios.get('/api/').then(
                    response => {
                        this.result = response.data;

                        // store the latest records' data in localStorage to load when there is no stock searched
                        localStorage.setItem("result", JSON.stringify(response.data));
                    }
                );
            }
        }
    },
    created: function() {
        this.loadRecords();
    }
}
</script>

<style scoped>

.msg {
    margin-top: 100px;
    padding: 20px 0;
    text-align: center;
    font-size: 14px;
}
@media (max-width: 576px) {
    .home {
        font-size: 9px;
    }
    .msg {
        font-size: 9px;
    }
}
</style>
