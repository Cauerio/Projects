<?php

namespace App\Http\Controllers;
use App\Http\Models\User;
use App\Models\User as ModelsUser;
use Illuminate\Http\Request;

class CRUDController extends Controller
{
    public function __invoke()
    {
        $index = ModelsUser::all();

        return $index;

        return view('index');
    }
        
    public function create()
    {
        return view('users.create');
    }
    
}
