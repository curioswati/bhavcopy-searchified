<template>
<div class="container">

    <div class="row search">
        <div class="col-md-1"></div>

        <div class="col-md-10">

            <form autocomplete="off">
                <div class="autocomplete input-group mb-3">
                    <input
                    name="search" class="form-control form-control-lg" type="text" placeholder="Type in a stock name..." aria-label="Search"
                    v-model="searchTerm" @keyup="autocomplete"
                    />
                    <!--div class="input-group-append">
                        <button class="btn btn-outline-secondary" type="submit" name="submit" v-on:click.prevent="getRecords">Go!</button>
                    </div-->
                </div>
                <ul v-if="suggestions" class="list-unstyled stock-list">
                    <li v-for="item in suggestions" :key="item" @click="getRecords" class="dropdown-item" :value=item>{{ item }}</li>
                </ul>
            </form>

        </div>

        <div class="col-md-1"></div>
    </div>

    <div v-if="recent" class="recent row">
        <div class="col-md-1"></div>
        <div class="col-md-10">
            Recently searched stocks:
            <button v-for="term, index in recent" :key="index" @click="getRecords" class="recent-term badge badge-light">
            {{term}}
            </button>
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
            recent: JSON.parse(localStorage.getItem("recent"))
        }
    },
    methods: {
        getRecords: function(event) {
            // get the current clicked stock name
            let stock_name = event.target.innerHTML.trim();

            axios.get('/api/records?name=' + stock_name).then(
                response => {

                  // send the received data to the parent component to insert in results.
                  this.$emit('loadRecords', response.data)

                  // get the recent search terms from local storage
                  let recent = JSON.parse(localStorage.getItem("recent"));

                  // if local storage doesn't have any recent searches, add the current one.
                  if (recent == null || Object.entries(recent).length == 0) {
                      recent = [stock_name];
                      localStorage.setItem("recent", JSON.stringify(recent));
                  }
                  // update the localstorage's search terms with the current one.
                  else if (!recent.includes(stock_name)) {
                      if (recent.length > 7) {
                          recent.shift();
                      }
                      recent.push(stock_name)
                      localStorage.setItem("recent", JSON.stringify(recent));
                  }

                  // remove the dropdown list when we selected an option.
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

                // clear previous suggestion list when the search box is empty.
                this.suggestions = null;

                // get the latest records' data stored in localStorage
                this.$emit('loadRecords', JSON.parse(localStorage.getItem('result')))
            }
        },
    }
}
</script>

<style scoped>
    .search {
        margin-top: 5vh;
    }
    .recent {
        padding-left: 18px;
    }
    .recent-term {
        margin: 0 0.8%;
        padding: 1% 1%;
        box-shadow: 1px 1px 3px 1px #f1f1f1;
        border: none;
        font-size: 11px;
    }
    .stock-list {
        margin-top: -18px;
        border-radius: 0 0 5px 5px;
    }
    .stock-list li {
        padding: 15px 15px;
        box-shadow: 2px 2px 10px 2px #f1f1f1;
    }
    @media (max-width: 576px) {
        .search .form-control {
            font-size: 10px;
        }
        .recent-term {
            font-size: 8px;
        }
    }
</style>
