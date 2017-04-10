This blueprint deploys a cockpit through ays

1. The [blueprint](https://github.com/gig-projects/playenv/blob/master/ays_cockpit/blueprints/1_cockpit.yaml) points to a very high-level abstracted blueprint servicetemplate
2. The [blueprint.cockpit](https://github.com/gig-projects/playenv/tree/master/ays_cockpit/servicetemplates/blueprint.cockpit) describes exactly what services are needed and how they relate to each other.

To use this blueprint, you'll need access to an ovc installation to deploy on top of.
Change parameters in the blueprint to reflect your installation.

To use ays:

1. Make sure you use the "ays_consume" branch on jumpscale_core8
2. do `ays init` to initialize your services structure
3. to install, do `ays install`
4. to destroy, do `ays destroy`
