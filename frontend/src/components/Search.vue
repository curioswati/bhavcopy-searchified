<template>
<div class="container">
    <div class="row">
        <div class="col-md-12" style="height:5vh;"></div>
    </div>
    <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-10">
            <form autocomplete="off">
                <div class="autocomplete input-group mb-3">
                    <input
                    name="search" class="form-control form-control-lg" type="text" placeholder="Type in a stock name..." aria-label="Search"
                    v-model="searchTerm" @keyup="autocomplete"
                    />
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="submit" name="submit" v-on:click.prevent="getRecords">Go!</button>
                    </div>
                </div>
                <ul v-if="suggestions" class="list-unstyled stock-list">
                    <li v-for="item in suggestions" @click="getRecords" class="dropdown-item" :value=item>{{ item }}</li>
                </ul>
            </form>
        </div>
        <div class="col-md-1"></div>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
    name: "Search",
    data: function () {
        return {
            searchTerm: '',
            suggestions: null,
        }
    },
    methods: {
        getRecords: function(event) {
            let stock_name = event.target.innerHTML;
            axios.get('/api/records?name=' + stock_name).then(
                response => {
                  this.$emit('loadRecords', response.data)
                  this.suggestions = null;
                }
            );
        },
        autocomplete: function() {
            if (this.searchTerm) {
                axios.get('/api/autocomplete?term=' + this.searchTerm).then(
                    response => {
                      this.suggestions = response.data;
                    }
                );
            }
            else {
                  this.suggestions = null;
            }
        },
    }
}
</script>
<style scoped>
    .stock-list {
        margin-top: -18px;
        border-radius: 0 0 5px 5px;
    }
    .stock-list li {
        padding: 15px 15px;
        box-shadow: 2px 2px 10px 2px #f1f1f1;
    }
</style>
