import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { StatsComponent } from './stats/stats.component';
import { LoginComponent } from './login/login.component';
import { ProfileComponent } from './profile/profile.component';
import { MeChallengeComponent } from './me-challenge/me-challenge.component';
import { WeChallengeComponent } from './we-challenge/we-challenge.component';
import { AboutComponent } from './about/about.component';
import { PastChallengesComponent } from './past-challenges/past-challenges.component';
import { UploadComponent } from './upload/upload.component';
import { PostComponent } from './post/post.component';
import { EditPostComponent } from './post/edit-post/edit-post.component';
import { SearchComponent } from './search/search.component';
import { EditProfileComponent } from './profile/edit-profile/edit-profile.component';
import { OtherProfComponent } from './other-prof/other-prof.component';
import { TaggedPostsComponent } from './tagged-posts/tagged-posts.component';


const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'stats', component: StatsComponent },
  { path: 'login', component: LoginComponent },
  { path: 'profile', component: ProfileComponent},
  { path: 'me-challenge', component: MeChallengeComponent },
  { path: 'we-challenge', component: WeChallengeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'past-challenges', component: PastChallengesComponent },
  { path: 'upload', component: UploadComponent },
  { path: 'search/:query', component: SearchComponent },
  { path: 'tagged/:query', component: TaggedPostsComponent },
  PostComponent.Route,
  EditPostComponent.Route,
  { path: 'profile/edit', component: EditProfileComponent},
  { path: ':displayName', component: OtherProfComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    scrollPositionRestoration: 'enabled',
    anchorScrolling: 'enabled'
  })],
  exports: [RouterModule]
})
export class AppRoutingModule {}