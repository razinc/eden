# BIOS
- Enable re-Size BAR support.
- Disable fast boot.

# BKM

- Pip
  ```
  python -m pip <pip arguments>
  ```
  
# Gaming

- [General setup.](https://www.reddit.com/r/linux_gaming/comments/zf6yer/setting_up_your_linux_gaming_system/)
- [MangoHUD setup.](https://www.reddit.com/r/linux_gaming/comments/gbrnj1/how_to_install_and_use_mangohud_with_game/)
- [`gamemodrun` setup.](https://www.reddit.com/r/linux/comments/1ff2aru/til_always_use_gamemoderun_for_proton_games/)
- Can’t change custom artwork on Steam? Remove from collection.

# Previous Issues

- [Prevent sleep when laptop lid is closed.](https://faq.i3wm.org/question/5629/how-to-prevent-sleep-on-laptop-lid-close/index.html)
   ```
   .
   .
   .
   [Login]
   HandleLidSwitch=ignore
   .
   .
   .
   ```
 - [Firefox keeps crashing.](https://www.reddit.com/r/firefox/comments/1ebygmt/firefox_crashing_on_fedora_40_with_and_without/)

   - Add this in `/etc/environment`
      ```
      MOZ_ENABLE_WAYLAND=0
      ```
      [Additional reference on Arch's Wiki.](https://wiki.archlinux.org/title/Firefox#Xwayland)
   - Test memory health.

# Testing

## [Stress Testing](https://wiki.archlinux.org/title/Stress_testing#MPrime)
- `mprime`: Check CPU health.
- `memtest86+`: Check memory stick health.

## General Monitoring
- `cpu-x`: Check if GPU ReBAR is enabled.
