<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        if(!Schema::hasTable('cache_test')){
        Schema::create('cache_test', function (Blueprint $table) {
            $table->engine = 'InnoDB';
            $table->string('clave')->primary();
            $table->mediumText('valor');
            $table->integer('expiration'); 
        });
    }
        if(!Schema::hasTable('cache_locks_test')){
        Schema::create('cache_locks_test', function (Blueprint $table) {
            $table->engine = 'InnoDB';
            $table->string('clave')->primary();
            $table->string('owner');
            $table->integer('expiration');
        });
    }
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('cache_test');
        Schema::dropIfExists('cache_locks_test');
    }
};